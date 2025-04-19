.PHONY: help run clean run_test

help:  ## Show help
	@grep -E '^[a-zA-Z_-]+:.*? ##' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'


run:  ## Init db and run the FastAPI app with Uvicorn
	# Remove old virtual environment and database
	rm -rf .dev_venv
	rm -f parts_unlimited_dev.db
	find . -type d -name '__pycache__' -exec rm -r {} +

	# Init db
	. scripts/init_db.sh

	# Init virtual environment
	python -m venv .dev_venv 
	. .dev_venv/bin/activate
	pip install -r dev_requirements.txt

	# Run migrations
	python -m app.db.migrations.part_description_words_frequency

	# Run app
	uvicorn app.main:app --reload


clean:  ## Remove Virtual Environment, DB and __pycache__
	rm -rf .dev_venv	
	rm -f parts_unlimited_dev.db
	find . -type d -name '__pycache__' -exec rm -r {} +


run_test: ## Run unit and integration tests
	# Remove old virtual environment and database
	rm -rf .dev_venv

	# Init virtual environment
	python -m venv .dev_venv 
	. .dev_venv/bin/activate
	pip install -r dev_requirements.txt

	# Run tests
	pytest -v --cov=app

	rm -rf .dev_venv
