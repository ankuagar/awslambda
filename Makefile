sls := ./node_modules/serverless/bin/serverless

deploy: require-stage require-account-id clean
	npm install
	${sls} deploy --stage=${stage}

require-stage:
ifndef stage
	@echo Invalid target
	@echo
	@echo "Stage is a required argument for this target"
	@echo "Usage: make target stage=<stage>"
	@echo "Valid options are test"
	@echo
	@exit 1
endif

require-account-id:
ifndef accountid
	@echo Invalid target
	@echo
	@echo "accountid is a required argument for this target"
	@echo "Usage: make target stage=<stage> accountid=<accountid>"
	@echo "Enter a valid account id"
	@echo
	@exit 1
endif

clean:
	rm -rf .requirements .serverless node_modules requirements.zip
