#####################################################
# Makefile containing shortcut commands for project #
#####################################################

.PHONY: tf-init
tf-init:
	docker-compose run --rm rony-ci terraform init

.PHONY: tf-fmt
tf-fmt:
	docker-compose run --rm rony-ci terraform fmt

.PHONY: tf-show
tf-show:
	docker-compose run --rm rony-ci terraform show

.PHONY: tf-validate
tf-validate:
	docker-compose run --rm rony-ci terraform validate

.PHONY: tf-plan
tf-plan:
	docker-compose run --rm rony-ci terraform plan

.PHONY: tf-apply
tf-apply:
	docker-compose run --rm rony-ci terraform apply

.PHONY: tf-destroy
tf-destroy:
	docker-compose run --rm rony-ci terraform destroy

.PHONY: tf-workspace-dev
tf-workspace-dev:
	docker-compose run --rm rony-ci terraform workspace select dev

.PHONY: tf-workspace-staging
tf-workspace-staging:
	docker-compose run --rm rony-ci terraform workspace select staging

.PHONY: tf-workspace-prod
tf-workspace-prod:
	docker-compose run --rm rony-ci terraform workspace select prod

.PHONY: tf-plan-cost
tf-plan-cost:
	docker-compose run --rm rony-ci plan-cost
