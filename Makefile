help:
	@echo "build-dev    - builds containers for services specified in docker-compose.dev.yml"
	@echo "build-tests  - builds containers for services specified in docker-compose.test.yml"
	@echo "start        - builds containers (if they do not exist already) and starts all services"
	@echo "stop         - stops all running containers belonging to the project"
	@echo "shell        - enter the shell of the application service"
	@echo "tests        - builds containers (if they do not exist already) and runs tests"


build-dev:
	docker-compose -f docker/docker-compose.dev.yml build

build-tests:
	docker-compose -f docker/docker-compose.test.yml build

start:
	docker-compose -f docker/docker-compose.dev.yml up

stop:
	docker-compose -f docker/docker-compose.dev.yml down -v

shell:
	docker-compose -f ./docker/docker-compose.dev.yml run --rm --service-ports app bash

.PHONY: tests
tests:
	docker-compose -f docker/docker-compose.test.yml run --rm --service-ports app-tests
