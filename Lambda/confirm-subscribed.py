import boto3
import os
from json import dumps, loads

def handler(event, context):
    print(event)
    table_name = os.environ["DYNAMO_TABLE"]
    email = loads(event["body"])["email"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    sns = boto3.client("sns",region_name="us-east-1")
    
    res_dynamo = table.get_item(
           Key={
               "email": email
           } 
    )
    item = res_dynamo["Item"]

    res = sns.get_subscription_attributes(
        SubscriptionArn=item["SubscriptionArn"]
    )
    if(res["Attributes"]["PendingConfirmation"]=="false"):
        res_dynamo = table.update_item(
            Key={
                "email": email
            },
            UpdateExpression="set Confirmed=:c",
            ExpressionAttributeValues={
                ":c": True
            },
            ReturnValues="NONE"
            )
        return {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            "body": dumps({ "Status": "Confirmed", "Mensage":"A confirmação foi feita"})}
    else:
        return {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
             "body": dumps({"Status": "Unconfirmed", "Mensage": "A confirmação não foi confirmada"})}