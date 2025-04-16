.PHONY: help run clean

help:  ## Show help
	@grep -E '^[a-zA-Z_-]+:.*? ##' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'


run:  ## Init db and run the FastAPI app with Uvicorn
	python scripts/init_db.py
	uvicorn app.main:app --reload

clean:  ## Remove DB and __pycache__

	rm -f parts_unlimited.db
	find . -type d -name '__pycache__' -exec rm -r {} +
