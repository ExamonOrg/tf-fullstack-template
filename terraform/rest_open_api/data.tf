data "aws_lambda_function" "examon_get_questions" {
  function_name = "examon_get_questions"
}

data "aws_lambda_function" "hello" {
  function_name = "hello"
}