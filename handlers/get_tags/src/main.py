import logging
import json


def lambda_handler(event, context):
    try:
        logging.debug("success")
        return {
            "statusCode": 200,
            "headers": {"content-type": "application/json"},
            "body": json.dumps({"tags": ["hello", "world2"]}),
        }
    except Exception as e:
        logging.error(e)
        return {"statusCode": 400, "body": {":(": ["hello", "world2"]}}
