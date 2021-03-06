.PHONY: default test-python test-pipenv run-drexeleds run-drexeleds-single run-wikiwatershed timing tolerance tolerance-single

PYTHON := $(shell command -v python 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)

default: test-python test-pipenv install run-drexeleds run-wikiwatershed timing tolerance

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
	bash -c "cd main; pipenv install"

run-drexeleds:
	bash -c "cd drexeleds; pipenv run python main.py"

run-drexeleds-single:
	bash -c "cd drexeleds; ls -1 ../tests/ | xargs -I name pipenv run python single.py name"

run-wikiwatershed:
	bash -c "cd wikiwatershed; pipenv run python main.py"

timing:
	bash -c "cd main; pipenv run python timing.py"

tolerance:
	bash -c "cd main; pipenv run python tolerance.py 0.00000000000001"

tolerance-single:
	bash -c "cd main; pipenv run python tolerance.py 0.00000000000001 --single"
