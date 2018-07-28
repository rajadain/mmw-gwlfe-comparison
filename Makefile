.PHONY: default test-python test-pipenv run-drexeleds run-wikiwatershed timing

PYTHON := $(shell command -v python 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)

default: test-python test-pipenv install run-drexeleds run-wikiwatershed timing

test-python:
ifndef PYTHON
	$(error "Please install python")
endif

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

timing:
	python timing.py
