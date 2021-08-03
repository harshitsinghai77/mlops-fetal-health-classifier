virtual_env:
	bash scripts/create_virtualenv.sh

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest

format:
	black *.py

predict:
	cd scripts && bash predict.sh

run_docker:
	bash scripts/run_docker.sh

lint:
	pylint --disable=R,C,W1203,E1101 mlib cli utilscli

all: install lint test