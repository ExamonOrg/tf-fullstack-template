#https://leejjon.medium.com/use-terraform-to-create-an-aws-lambda-function-that-runs-your-typescript-code-b805db667a93
build: clean package zip
.PHONY: build

test:
	npm run test
.PHONY: tests

package:
	 npm i && \
  npm run build && \
  npm prune --production &&\
  mkdir -p dist &&\
  cp -r ./src/*.js dist/ &&\
  cp -r ./node_modules dist/ &&\
  cp -r ./index.js dist/ &&\
  cd dist &&\
  find . -name "*.zip" -type f -delete
.PHONY: package

zip:
	zip -r ${package_name} package/
.PHONY: zip

clean:
	rm -rf node_modules && \
	rm -rf ${package_name}
.PHONY: clean
