#!/bin/bash
set -e

cd pet/create
make --file=../../lambda_python.mk package_name=pet_create.zip clean

cd ../delete
make --file=../../lambda_python.mk package_name=pet_delete.zip clean

cd ../get
make --file=../../lambda_python.mk package_name=pet_get.zip clean

cd ../index
make --file=../../lambda_python.mk package_name=pet_index.zip clean

cd ../update
make --file=../../lambda_python.mk package_name=pet_update.zip clean