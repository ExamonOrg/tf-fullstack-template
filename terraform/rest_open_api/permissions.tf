resource "aws_lambda_permission" "permission_1" {
  statement_id  = "AllowExecutionFromRestAPI_${data.aws_lambda_function.examon_get_questions.function_name}"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.examon_get_questions.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.default.execution_arn}/*/*"
}

resource "aws_lambda_permission" "permission_2" {
  statement_id  = "AllowExecutionFromRestAPI_${data.aws_lambda_function.hello.function_name}"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.hello.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.default.execution_arn}/*/*"
}

resource "aws_lambda_permission" "permission_3" {
  statement_id  = "AllowExecutionFromRestAPI_${data.aws_lambda_function.examon_get_tags.function_name}"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.examon_get_tags.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.default.execution_arn}/*/*"
}