.PHONY: install test format lint all

install:
	pip install --upgrade pip &&\
		pip install --force-reinstall -r requirements.txt

test:
	python -m pytest -vv --cov=src
	# --cov specify the root folder for 

format:
	black src/*.py test/*.py

lint:
	pylint --disable=R,C src/*.py test/*.py

refactor: format lint

all: install format lint test