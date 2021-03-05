import json
import os
import boto3

def handler(event,context):
    data = json.loads(event["body"])
    dynamodb = boto3.client("dynamodb")
    if("username" in data) and ("password" in data): 
        username = data["username"]
        password = data["password"]

        table_name = os.environ["DYNAMO_TABLE"]
        table = dynamodb.Table(table_name)

        