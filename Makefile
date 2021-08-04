virtual_env:
	bash scripts/create_virtualenv.sh

install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

install_dev:
	pip3 install -r requirements-dev.txt

test:
	pytest

format:
	black *.py

predict:
	cd scripts && bash predict.sh

build_docker:
	bash scripts/run_docker.sh

run_docker:
	docker run --rm -p 8000:8000 harshitsinghai77/fetal-health-classifier

lint:
	pylint --disable=C,R0914,E1136 model cli utilscli

docker_lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

all: install lint test