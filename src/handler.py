import boto3
import jinja2
import json
import logging
import time
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda1(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    logger.info("Service wide environment variable value is {}".format(os.getenv('service_wide_env_variable')))
    logger.info("Function specific environment variable value is {}".format(os.getenv('my_simple_lambda_function_env_variable')))
    logger.info("Response is {}".format(response))
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def lambda2(event, context):
    # 20 mins = 1200 seconds. This lambda function will terminate with a timeout. See serverless.yml
    # Default timeout is 6 seconds. And on setting a value > 900sec you will get an error during deployment:
    #An error occurred: MyDashsimpleDashlambdaDashfunctionLambdaFunction - 1 validation error detected: Value '1200' at 'timeout' failed to satisfy constraint: Member must have value less than or equal to 900 (Service: AWSLambdaInternal; Status Code: 400; Error Code: ValidationException; Request ID: b2debad7-3ee6-432f-a3ce-c18592332371).
    logger.info("Received event is {}".format(event)) # {key1: value1, key2: value2 } is passed in as event
    logger.info("Service wide environment variable is {}".format(os.getenv('service_wide_env_variable')))
    logger.info("Function specific environment variable value is {}".format(os.getenv('lambda_that_simply_sleeps_env_variable')))
    logger.info("Received context is {}".format(context))
    for i in range(1200):
        logger.info("Iteration {}".format(i))
        time.sleep(1)

# def lambda3(event, context):
#     logger.info("Received event is {}".format(event))
#     client = boto3.client('lambda')
