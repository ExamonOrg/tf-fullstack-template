variable lambda_configs {
  description = "Lambda Configurations"
  type        = list(object({
    source_path = string
    name        = string
    memory_size = string
  }))
  default = [
    {
      source_path = "handlers/pet/create/package",
      name        = "petshop_create_pet",
      memory_size = 768
    },
    {
      source_path = "handlers/pet/delete/package",
      name        = "petshop_delete_pet",
      memory_size = 768
    },
    {
      source_path = "handlers/pet/index/package",
      name        = "petshop_index_pet",
      memory_size = 768
    },
    {
      source_path = "handlers/pet/get/package",
      name        = "petshop_get_pet",
      memory_size = 768
    },
    {
      source_path = "handlers/pet/update/package",
      name        = "petshop_update_pet",
      memory_size = 768
    },
  ]
}

module "lambdas" {
  for_each    = {for i, v in var.lambda_configs :  i => v}
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../${each.value.source_path}"
  name        = each.value.name
  memory_size = each.value.memory_size
}

module "permission" {
  source          = "../../../tf-modules/api_gw_lambda_permission"
  for_each        = {for i, v in var.lambda_configs :  i => v}
  function_name   = each.value.name
  api_gateway_arn = module.restapi.execution_arn
}