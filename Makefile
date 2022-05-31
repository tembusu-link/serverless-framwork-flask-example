.PHONY: clean-pyc clean-build docs

COMMIT_ID = $(shell git rev-parse HEAD)
COMMIT_MSG = $(shell git log -1 --pretty=%B)
VERSION = $(shell grep "current_version" .bumpversion.cfg | cut -d' ' -f3-)


deploy-dev:
	serverless deploy function --function api --stage dev

deploy-production:
	serverless deploy function --function api --stage production