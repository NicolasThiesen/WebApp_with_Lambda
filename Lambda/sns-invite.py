import boto3
import json
import os

def handler(event, context):
    sns_arn = os.environ["SNS_ARN"]
    table_name = os.environ["DYNAMO_TABLE"]
    email = event["email"]
    mensage = event["mensage"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    sns = boto3.client("sns",region_name="us-east-1")

    res_dynamo = table.get_item(
        Key={
            "email": email
        } 
    )
    item = res_dynamo["Item"]

    sns.publish(
        TopicArn=sns_arn
        TargetArn=item[""]
    )