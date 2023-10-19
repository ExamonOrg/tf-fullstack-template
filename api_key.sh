cd terraform/site

API_KEY=$(terraform output -raw api_key_value)
INVOKE_URL=$(terraform output -raw invoke_url)

echo "curl -H \"x-api-key: ${API_KEY}\" ${INVOKE_URL}v1/pets"
echo "curl -H \"x-api-key: ${API_KEY}\" ${INVOKE_URL}v1/pet"
