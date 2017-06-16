dev-build:
	docker-compose build

update-time:
	docker-machine ssh default "sudo ntpclient -s -h pool.ntp.org"

bootstrap:
	make dev-build

test:
	docker-compose run --name {{cookiecutter.repo_name}}_tests --rm {{cookiecutter.repo_name}} py.test --strict $${TEST_ARGS:-"tests/"}

shell:
	docker-compose run --name {{cookiecutter.repo_name}}_shell --rm pyiptis python3
