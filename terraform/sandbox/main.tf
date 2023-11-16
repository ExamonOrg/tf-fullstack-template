module "my_dynamodb" {
  source              = "../../../tf-modules/dynamodb"
  table_name          = "test"
  hash_key            = "uuid"
  enable_streams      = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  dynamodb_attributes = tolist([
    {
      name = "uuid"
      type = "S"
    }
  ])
}
