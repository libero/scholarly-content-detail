
start:
	docker-compose up

stop:
	docker-compose down -v

shell:
	docker-compose run --rm --service-ports app bash
