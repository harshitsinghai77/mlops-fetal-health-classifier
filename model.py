"""MLOps Library"""

import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    classification_report,
    precision_score,
    f1_score,
)
import logging

from utils.constant import FETAL_HEALTH_DICT

logging.basicConfig(level=logging.INFO)


def load_model(model="model.joblib"):
    """Grabs model from disk"""

    clf = joblib.load(model)
    return clf


def data(fname="dataset/fetal_health.csv"):
    """Load and returns the training data."""
    df = pd.read_csv(fname)
    return df


def get_best_model(X_train, y_train):
    """Train Multiple model on the training set and return the model with the best cross_val_score.

    A quick model selection process
    Train using LogisticRegression, DecisionTreeClassifier, RandomForestClassifier, SVC
    """
    pipeline_lr = Pipeline(
        [("logistic_regression", LogisticRegression(random_state=42))]
    )
    pipeline_dt = Pipeline([("decision_tree", DecisionTreeClassifier(random_state=42))])
    pipeline_rf = Pipeline([("random_forest", RandomForestClassifier())])
    pipeline_svc = Pipeline([("sv_classifier", SVC())])

    # List of all the pipelines
    pipelines = [pipeline_lr, pipeline_dt, pipeline_rf, pipeline_svc]

    # Dictionary of pipelines and classifier types for ease of reference
    pipe_dict = {
        0: "Logistic Regression",
        1: "Decision Tree",
        2: "RandomForest",
        3: "SVC",
    }

    # Fit the pipelines
    for pipe in pipelines:
        pipe.fit(X_train, y_train)

    # cross validation on accuracy
    cv_results_accuracy = []
    cv_result_mean = []
    for i, model in enumerate(pipelines):
        cv_score = cross_val_score(model, X_train, y_train, cv=10)
        cv_results_accuracy.append(cv_score)
        cv_mean = cv_score.mean()
        cv_result_mean.append(cv_score.mean())
        print("%s: %f " % (pipe_dict[i], cv_mean))

    # Getting the best estimator
    max_value = max(cv_result_mean)
    max_index = cv_result_mean.index(max_value)
    return pipelines[max_index]


def get_grid_search_best_parameters(X_train, y_train):
    # Building a dictionalry with list of optional values that will me analyesed by GridSearch CV
    parameters = {
        "n_estimators": [100, 150, 200, 500, 700, 900],
        "max_features": ["auto", "sqrt", "log2"],
        "max_depth": [4, 6, 8, 12, 14, 16],
        "criterion": ["gini", "entropy"],
        "n_jobs": [-1, 1, None],
    }

    # Fitting the trainingset to find parameters with best accuracy

    grid_search_clf = GridSearchCV(
        estimator=RandomForestClassifier(), param_grid=parameters, cv=5, verbose=1
    )
    grid_search_clf.fit(X_train, y_train)
    # Getting the outcome of gridsearch

    return grid_search_clf.best_params_


def model_metrics(classifier_name, y_test, predictions):
    """Print Metrics of the model."""
    acccuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions, average="weighted")
    precision = precision_score(y_test, predictions, average="weighted")
    f1 = f1_score(y_test, predictions, average="micro")

    print(f"********* {classifier_name} Results *********")
    print("Accuracy    : ", acccuracy)
    print("Recall      : ", recall)
    print("Precision   : ", precision)
    print("F1 Score    : ", f1)
    print(classification_report(y_test, predictions))
    return acccuracy


def retrain(model_name="model.joblib"):
    """Retrains the model

    See the notebook: Fetal Health Classification.ipynb
    """

    df = data()
    # assigning values to features as X and target as y
    X = df.drop(["fetal_health"], axis=1)
    y = df["fetal_health"]

    # Set up a standard scaler for the features
    col_names = list(X.columns)
    scaler = StandardScaler()
    X_df = scaler.fit_transform(X)
    X_df = pd.DataFrame(X_df, columns=col_names)

    # spliting test and training sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_df, y, test_size=0.3, random_state=42
    )

    # returns a pipeline object
    best_model = get_best_model(X_train, y_train)
    classifier_name = best_model.steps[0][0]
    classifier = best_model.steps[0][1]
    print(f"Using {classifier_name} classifier as best model.")

    predictions = classifier.predict(X_test)
    accuracy = model_metrics(classifier_name, y_test, predictions)

    logging.debug(f"Model Accuracy: {accuracy}")
    joblib.dump(classifier, model_name)
    return accuracy, model_name


def format_input(payload):
    """Takes int and converts to numpy array"""
    features = pd.DataFrame(payload, index=[0])
    return features


def scale_input(val):
    """Scales input to training feature values"""

    df = data()
    features = df.drop(["fetal_health"], axis=1)
    input_scaler = StandardScaler().fit(features)
    scaled_input = input_scaler.transform(val)
    return scaled_input


def human_readable_payload(predict_value):
    """Takes numpy array and returns back human readable dictionary
    'fetal_health' Tagged as 1 (Normal), 2 (Suspect) and 3 (Pathological)
    """
    predict_value = int(predict_value[0])
    result = {
        "prediction": predict_value,
        "prediction_label": FETAL_HEALTH_DICT[predict_value],
    }
    return result


def predict(payload):
    """Takes weight and predicts height"""

    clf = load_model()  # loadmodel
    payload = format_input(payload)
    scaled_input_result = scale_input(payload)  # scale feature input
    fetal_health_prediction = clf.predict(scaled_input_result)  # scaled prediction
    result = human_readable_payload(fetal_health_prediction)
    return result
