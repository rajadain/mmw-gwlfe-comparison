.PHONY: default test-pipenv run-drexeleds run-wikiwatershed

PIPENV := $(shell command -v pipenv 2> /dev/null)

default: test-pipenv install run-drexeleds run-wikiwatershed

test-pipenv:
ifndef PIPENV
	$(error "Please install pipenv")
endif

install:
	bash -c "cd drexeleds; pipenv install"
	bash -c "cd wikiwatershed; pipenv install"

run-drexeleds:
	bash -c "cd drexeleds; pipenv run python main.py"

run-wikiwatershed:
	bash -c "cd wikiwatershed; pipenv run python main.py"
