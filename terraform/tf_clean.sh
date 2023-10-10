#!/bin/bash
set -e

cd api_domain
terraform destroy -auto-approve

cd ../rest_open_api
terraform destroy -auto-approve

cd ../lambdas
terraform destroy -auto-approve