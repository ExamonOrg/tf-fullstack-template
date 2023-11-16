package_dir := package
s3_bucket := examon-lambdas
lambda_prefix := petshop

export PYTHONPATH := .

build: clean package zip
.PHONY: build

deploy: build upload_fn
.PHONY: build

test:
	poetry run pytest
.PHONY: tests

package:
	rm -rf ${package_dir} && \
	poetry config virtualenvs.in-project true && \
    poetry install && \
	mkdir -p ${package_dir} && \
    poetry export --without-hashes --format requirements.txt --output ${package_dir}/requirements.txt && \
    poetry run pip install --no-deps --upgrade --cache-dir ./.pip_cache --requirement ${package_dir}/requirements.txt --target package && \
    cp -R src ${package_dir}
.PHONY: package

upload_fn:
	aws s3 cp ${name}.zip s3://${s3_bucket} && \
	aws lambda update-function-code --function-name ${lambda_prefix}_${name} --s3-bucket ${s3_bucket} --s3-key ${name}.zip > /dev/null
.PHONY: deploy

zip:
	cd package && \
	zip -r -D --exclude requirements.\* --recurse-paths ${name}.zip * && \
	cd .. && \
	mv package/${name}.zip .
.PHONY: zip

clean:
	rm -rf ${package_dir} && \
	rm -rf ./.pip_cache && \
	rm -rf ./.pytest_cache && \
	rm -rf ./.venv && \
	rm -rf ./*.zip && \
	rm -rf ./__pycache__
.PHONY: clean
