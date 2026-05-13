.PHONY: test lint type cov complexity all

test:
	pytest -v

cov:
	pytest --cov=. --cov-report=term-missing --cov-report=html

lint:
	ruff check .

type:
	mypy --strict .

complexity:
	radon cc . -s -a

all: lint type test cov complexity