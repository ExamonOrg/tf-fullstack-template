module "petshop_pet_create_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/pet/create/package"
  name        = "petshop_create_pet"
  memory_size = 768
}

module "petshop_pet_delete_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/pet/delete/package"
  name        = "petshop_delete_pet"
  memory_size = 768
}


module "petshop_pet_get_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/pet/get/package"
  name        = "petshop_get_pet"
  memory_size = 768
}


module "petshop_pet_index_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/pet/index/package"
  name        = "petshop_index_pet"
  memory_size = 768
}


module "petshop_pet_update_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/pet/update/package"
  name        = "petshop_pet_update"
  memory_size = 768
}
