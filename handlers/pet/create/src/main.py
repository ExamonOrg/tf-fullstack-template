import json

import boto3

from aws_lambda_powertools import Metrics
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger

logger = Logger(log_uncaught_exceptions=True, service="pet")
tracer = Tracer()
metrics = Metrics(namespace="petshop.create")

from uuid import uuid4

region = 'eu-west-1'


@logger.inject_lambda_context(
    correlation_id_path="headers.my_request_id_header",
    log_event=True,
)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context):
    logger.info(f"--1 event: {event}")
    logger.info(f"--2 context: {context}")
    logger.info(f"--3 keys: {event.keys()}")
    body = json.loads(event['body'])
    logger.info(f"--4 body: {body}")

    try:
        dynamodb = boto3.resource('dynamodb', region_name=region)
        table = dynamodb.Table('pets')
        pet_uuid = uuid4()
        response = table.put_item(
            Item={
                'pet_uuid': str(pet_uuid),
                'name': body['name'],
                'breed': body['breed']
            }
        )
        logger.info(response)
        logger.info(f"successfully created pet: {pet_uuid}")
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        return {
            "statusCode": status_code,
            "headers": {"content-type": "application/json"}
        }
    except Exception as e:
        logger.error(e)
        raise
