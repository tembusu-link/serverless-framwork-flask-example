.PHONY: clean-pyc clean-build docs

COMMIT_ID = $(shell git rev-parse HEAD)
COMMIT_MSG = $(shell git log -1 --pretty=%B)
VERSION = $(shell grep "current_version" .bumpversion.cfg | cut -d' ' -f3-)


push:
	rsync -avzP -e "ssh -p 2224" -rt --delete  --exclude '.*' --exclude 'node_modules' --exclude '*.pyc' . wangsha@kg.aws:/home/wangsha/serverless-framework-test

pull:
	rsync -avzP -e "ssh -p 2224" -rt --exclude 'node_modules' wangsha@kg.aws:/home/wangsha/serverless-framework-test/* .

deploy-aws:
	serverless deploy function --function api