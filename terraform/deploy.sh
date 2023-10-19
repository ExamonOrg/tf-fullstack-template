#!/bin/bash
set -e

cd site
terraform init
terraform plan -out=plan.out
terraform apply plan.out
