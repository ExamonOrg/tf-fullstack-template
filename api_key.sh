cd terraform/rest_open_api

API_KEY=$(terraform output -raw api_key_value)
INVOKE_URL=$(terraform output -raw invoke_url)

echo "curl -H \"x-api-key: ${API_KEY}\" ${INVOKE_URL}v1/hello"
echo "curl -H \"x-api-key: ${API_KEY}\" ${INVOKE_URL}v1/tags"
echo "curl -H \"x-api-key: ${API_KEY}\" ${INVOKE_URL}v1/questions"