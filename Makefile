PYTHON ?= python3

.PHONY: run test

run:
	$(PYTHON) app.py

test:
	$(PYTHON) -m unittest discover -s tests -v
