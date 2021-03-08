import boto3
import os

def handler(event, context):
    table_name = os.environ["DYNAMO_TABLE"]
    email = event["email"]

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
        res_dynamo = table.put_item(
            Item={
                "email": email,
                "Confirmed": True
            }
        )
        return {"Status": "Confirmed", "Mensage":"A confirmação foi feita"}
    else:
        return {"Status": "Unconfirmed", "Mensage": "A confirmação não foi confirmada"}