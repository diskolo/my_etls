.PHONY: format
format:  ## Format python code
	poetry run ruff format

.PHONY: check-format
check-format:  ## Check format python code
	poetry run ruff format --check