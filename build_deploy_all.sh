#!/bin/bash
set -e

cd handlers
sh build.sh

cd ../terraform
sh deploy.sh