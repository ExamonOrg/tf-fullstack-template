module "permission_1" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  function_name   = module.petshop_pet_create_lambda.function_name
  api_gateway_arn = module.restapi.execution_arn
}

module "permission_2" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  function_name   = module.petshop_pet_delete_lambda.function_name
  api_gateway_arn = module.restapi.execution_arn
}

module "permission_3" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  function_name   = module.petshop_pet_index_lambda.function_name
  api_gateway_arn = module.restapi.execution_arn
}

module "permission_4" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  function_name   = module.petshop_pet_update_lambda.function_name
  api_gateway_arn = module.restapi.execution_arn
}

module "permission_5" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  function_name   = module.petshop_pet_get_lambda.function_name
  api_gateway_arn = module.restapi.execution_arn
}