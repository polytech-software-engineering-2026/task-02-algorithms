.PHONY: install hooks lint format test check check-volume ref-tests

install:
	uv sync

hooks:
	uv run pre-commit install

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy tasks

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest tests -q

# то же, что тесты в CI: свои тесты + эталонные тесты преподавателя
ref-tests:
	uv run pytest tests tests_reference -q

check: lint ref-tests

check-volume:
	uv run python scripts/check_volume.py
