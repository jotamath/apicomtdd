run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

#TODO: teste de schemas 00:19