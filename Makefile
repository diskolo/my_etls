.PHONY: format
format:  ## Format python code
	poetry run ruff format

.PHONY: check-format
check-format:  ## Check format python code
	poetry run ruff format --check


.PHONY: test-unit
test-unit: ## Run unit tests
	poetry run pytest -n auto tests/unit -ra

.PHONY: test-integration
test-integration: ## Run integration tests
	poetry run pytest tests/integration -ra

.PHONY: test
test: test-unit test-integration ## Run all the tests