module "get_questions_lambda" {
  source      = "../../../tf-modules/lambda_ot"
  source_dir  = "${path.module}/../../handlers/get_questions/package"
  name        = "examon_get_questions"
  memory_size = 768
}

module "get_tags_lambda" {
  source     = "../../../tf-modules/lambda_ot"
  source_dir = "${path.module}/../../handlers/get_tags/package"
  name       = "examon_get_tags"
}

module "get_hello_lambda" {
  source     = "../../../tf-modules/lambda"
  source_dir = "${path.module}/../../handlers/hello"
  name       = "hello"
  handler    = "index.handler"
  runtime    = "nodejs18.x"
}



