.PHONY: help bootstrap lint test clean

VENV=.venv
PYTHON=$(VENV)/bin/python

help:
	@echo "Available targets:"
	@echo "  bootstrap - prepare virtual environment and install dependencies"
	@echo "  lint      - run static code analysis"
	@echo "  test      - run project tests"
	@echo "  clean     - remove virtual environment and development artifacts"

bootstrap: $(PYTHON)
$(PYTHON):
	python -m venv $(VENV)
	$(VENV)/bin/python -m pip install pip==24.1.2 setuptools==70.3.0 wheel==0.43.0
	$(VENV)/bin/python -m pip install -e .[dev]

lint: bootstrap
	$(PYTHON) -m ruff check --fix .

test: bootstrap
	$(PYTHON) manage.py test --settings=sugar.test_settings

clean:
	rm -rf $(VENV) sugar.egg-info .ruff_cache
	find ./ -name "__pycache__" -type d | xargs rm -rf
