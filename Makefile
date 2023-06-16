.PHONY: up build down

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down
