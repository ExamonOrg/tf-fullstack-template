cd pet/create
make --file=../../lambda_python.mk package_name=pet_create.zip build

cd ../delete
make --file=../../lambda_python.mk package_name=pet_delete.zip build

cd ../get
make --file=../../lambda_python.mk package_name=pet_get.zip build

cd ../index
make --file=../../lambda_python.mk package_name=pet_index.zip build

cd ../update
make --file=../../lambda_python.mk package_name=pet_update.zip build