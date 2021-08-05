import requests
import json

# URL for the web service
scoring_uri = (
    "http://5534d0ff-e421-4bee-bcb1-aa8d66be732d.centralindia.azurecontainer.io/score"
)

# Sample data to score, strictly tied to the input of the trained model
data = {
    "data": [
        {
            "baseline value": 130.0,
            "accelerations": 0.005,
            "fetal_movement": 0.469,
            "uterine_contractions": 0.005,
            "light_decelerations": 0.004,
            "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.001,
            "abnormal_short_term_variability": 29.0,
            "mean_value_of_short_term_variability": 1.7,
            "percentage_of_time_with_abnormal_long_term_variability": 0.0,
            "mean_value_of_long_term_variability": 7.8,
            "histogram_width": 112.0,
            "histogram_min": 65.0,
            "histogram_max": 177.0,
            "histogram_number_of_peaks": 6.0,
            "histogram_number_of_zeroes": 1.0,
            "histogram_mode": 133.0,
            "histogram_mean": 129.0,
            "histogram_median": 133.0,
            "histogram_variance": 27.0,
            "histogram_tendency": 0.0,
        },
        {
            "baseline value": 150.0,
            "accelerations": 0.0,
            "fetal_movement": 0.0,
            "uterine_contractions": 0.003,
            "light_decelerations": 0.0,
            "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0,
            "abnormal_short_term_variability": 61.0,
            "mean_value_of_short_term_variability": 0.9,
            "percentage_of_time_with_abnormal_long_term_variability": 3.0,
            "mean_value_of_long_term_variability": 8.7,
            "histogram_width": 28.0,
            "histogram_min": 138.0,
            "histogram_max": 166.0,
            "histogram_number_of_peaks": 0.0,
            "histogram_number_of_zeroes": 0.0,
            "histogram_mode": 152.0,
            "histogram_mean": 153.0,
            "histogram_median": 155.0,
            "histogram_variance": 3.0,
            "histogram_tendency": 0.0,
        },
        {
            "baseline value": 123.0,
            "accelerations": 0.0,
            "fetal_movement": 0.0,
            "uterine_contractions": 0.007,
            "light_decelerations": 0.002,
            "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.002,
            "abnormal_short_term_variability": 26.0,
            "mean_value_of_short_term_variability": 4.3,
            "percentage_of_time_with_abnormal_long_term_variability": 0.0,
            "mean_value_of_long_term_variability": 19.4,
            "histogram_width": 146.0,
            "histogram_min": 50.0,
            "histogram_max": 196.0,
            "histogram_number_of_peaks": 8.0,
            "histogram_number_of_zeroes": 1.0,
            "histogram_mode": 126.0,
            "histogram_mean": 105.0,
            "histogram_median": 113.0,
            "histogram_variance": 117.0,
            "histogram_tendency": 0.0,
        },
    ]
}

# Convert to JSON
input_data = json.dumps(data)

# Set the content type
headers = {"Content-Type": "application/json"}

try:
    # Make the request and display the response
    resp = requests.post(scoring_uri, input_data, headers=headers)
    predictions = resp.json()
    print(predictions)


except requests.exceptions.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", "ignore")))
