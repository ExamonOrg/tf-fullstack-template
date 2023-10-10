variable "api_name" {
  default = "rest-api"
}

variable "put_rest_api_mode" {
  default = "merge"
}

variable "open_api_json_relative_path" {
  default = "../../api_specification/openapi.json"
}

variable "aws_region" {
  default = "eu-west-1"
}

variable "stage_name" {
  default = "vi"
}

variable "terraform_state_bucket" {
  default = "examon-terraform-state"
}

variable "terraform_state_key" {
  default = "rest-open-api/terraform.tfstate"
}
