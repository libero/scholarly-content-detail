help:
	@echo "start  - builds and/or starts all services"
	@echo "stop   - stops all running containers belonging to the project"
	@echo "shell  - enter the shell of the application service"

start:
	docker-compose -f docker/docker-compose.dev.yml up

stop:
	docker-compose -f docker/docker-compose.dev.yml down -v

.PHONY: tests
tests:
	docker-compose -f docker/docker-compose.test.yml run --rm --service-ports app-tests

shell:
	docker-compose -f ./docker/docker-compose.dev.yml run --rm --service-ports app bash
