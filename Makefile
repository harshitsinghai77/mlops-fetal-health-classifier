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
	pylint --disable=C,R0914,E1136 model cli utilscli

docker_lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

all: install lint test