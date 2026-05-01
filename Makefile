.PHONY: install lint typecheck test all

install:
	pip install -e ".[dev]"

lint:
	ruff check src tests scripts
	ruff format --check src tests scripts

format:
	ruff format src tests scripts
	ruff check --fix src tests scripts

typecheck:
	mypy src/rugiet_ltv

test:
	pytest tests/

all: lint typecheck test
