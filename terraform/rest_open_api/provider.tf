terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
  backend "s3" {
    bucket = "examon-terraform-state"
    key    = "rest-open-api/terraform.tfstate"
    region = "eu-west-1"
  }
}