# Variables
PYTHON := python3
APP_NAME := myapp
TEST_PATH := tests/

.PHONY: help
help:  ## Show this help message
	@echo "Available commands for $(APP_NAME):"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

# Environment setup
.PHONY: install
install:  ## Install all dependencies
	$(PYTHON) -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: dev-setup
dev-setup: install  ## Complete development setup
	pre-commit install
	@echo "✅ Development environment ready!"

# Code quality
.PHONY: format
format:  ## Format code
	black $(APP_NAME) $(TEST_PATH)
	isort $(APP_NAME) $(TEST_PATH)

.PHONY: lint
lint:  ## Run linting
	flake8 $(APP_NAME) $(TEST_PATH)
	black --check $(APP_NAME) $(TEST_PATH)
	isort --check-only $(APP_NAME) $(TEST_PATH)

# Testing
.PHONY: test
test:  ## Run tests
	$(PYTHON) -m pytest $(TEST_PATH) -v

.PHONY: test-watch
test-watch:  ## Run tests in watch mode
	$(PYTHON) -m pytest $(TEST_PATH) -v --looponfail

.PHONY: coverage
coverage:  ## Run tests with coverage
	$(PYTHON) -m pytest $(TEST_PATH) --cov=$(APP_NAME) --cov-report=html --cov-report=term

# Development
.PHONY: serve
serve:  ## Start development server
	flask --app $(APP_NAME) run --debug --reload

.PHONY: shell
shell:  ## Start application shell
	flask --app $(APP_NAME) shell

# Database
.PHONY: db-migrate
db-migrate:  ## Create database migration
	flask --app $(APP_NAME) db migrate

.PHONY: db-upgrade
db-upgrade:  ## Apply database migrations
	flask --app $(APP_NAME) db upgrade

# Cleanup
.PHONY: clean
clean:  ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build/ dist/ *.egg-info/ htmlcov/ .coverage .pytest_cache/

# All-in-one commands
.PHONY: check
check: lint test  ## Run all checks

.PHONY: fresh-start
fresh-start: clean install  ## Clean everything and reinstall
