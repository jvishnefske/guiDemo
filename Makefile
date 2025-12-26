.PHONY: test coverage lint clean

test:
	python -m pytest tests/ -v

coverage:
	python -m pytest tests/ --cov=. --cov-report=html --cov-report=xml

lint:
	python -m flake8 main.py --ignore=E501
	python -m pylint main.py --exit-zero

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov coverage.xml *.pyc
