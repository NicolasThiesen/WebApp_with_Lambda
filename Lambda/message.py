import boto3
import os
from json import dumps,loads

def handler(event, context):
    print(event)
    sns_arn = os.environ["SNS_ARN"]

    sub = loads(event["body"])["subject"]
    message = loads(event["body"])["message"]

    sns = boto3.client("sns",region_name="us-east-1")

    res = sns.publish(
        TopicArn=sns_arn,
        Message=message,
        Subject=sub
    )
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        "body": dumps({"Status": "Mensagem enviada com sucesso"})}