#!/bin/bash
set -e

cd site
terraform destroy -auto-approve
