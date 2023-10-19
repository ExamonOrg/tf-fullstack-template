import json
import re

from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Logger

from aws_lambda_powertools.middleware_factory import lambda_handler_decorator

logger = Logger()
metrics = Metrics(namespace="examon.get_questions")
tracer = Tracer()


def log_uuid_values(data, path=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f'{path}.{key}' if path else key
            if isinstance(value, (dict, list)):
                log_uuid_values(value, new_path)
            elif isinstance(value, str) and re.search(r'uuid', key):
                logger.info(f'{new_path}: {value}')
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f'{path}[{i}]'
            log_uuid_values(item, new_path)


@lambda_handler_decorator
def middleware_before_after(handler, event, context):
    # logic_before_handler_execution()
    log_uuid_values(event)
    response = handler(event, context)
    # logic_after_handler_execution()
    return response


@tracer.capture_method
def a_method() -> bool:
    tracer.put_annotation(key="a_method", value='??')
    return False


example = {
    'id': '1234',
    'name': 'John Doe',
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    },
    'uuid1': '123e4567-e89b-12d3-a456-426655440000',
    'uuid2': '456e1234-e89b-12d3-a456-426655440000',
    'nested': {
        'uuid3': '789e1234-e89b-12d3-a456-426655440000',
        'list': [
            'abcde1234-e89b-12d3-a456-426655440000',
            'fghij5678-e89b-12d3-a456-426655440000'
        ]
    },
    'list': [
        {
            'uuid4': 'klmno1234-e89b-12d3-a456-426655440000'
        },
        {
            'uuid5': 'pqrst5678-e89b-12d3-a456-426655440000'
        }
    ]
}


@logger.inject_lambda_context(
    correlation_id_path="headers.my_request_id_header",
    log_event=True
)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext):
    a_method()
    try:
        log_uuid_values(event)
        log_uuid_values(example)
        logger.info(f"Log Message {logger.get_correlation_id()}")
        tracer.put_annotation(key="TracingId", value='1')
        metrics.add_metric(name="GetQuestion", unit=MetricUnit.Count, value=1)
        tracer.put_metadata(key="MetaData",
                            value={
                                "request_id": context.aws_request_id,
                                "function_name": context.function_name,
                                "function_version": context.function_version,
                                "invoked_function_arn": context.invoked_function_arn,
                                "memory_limit_in_mb": context.memory_limit_in_mb
                            })
        return {
            "statusCode": 200,
            "headers": {"content-type": "application/json"},
            "body": json.dumps({"message": "question 2"}),
        }
    except Exception as e:
        Logger.error(e)
        return {"code": 400, "message": "Error"}
