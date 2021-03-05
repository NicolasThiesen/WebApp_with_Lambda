import json
import os
import boto3

def handler(event,context):
    data = json.loads(event["body"])
    dynamodb = boto3.resource("dynamodb")
    if("email" in data) and ("password" in data): 
        email = data["email"]
        password = data["password"]

        table_name = os.environ["DYNAMO_TABLE"]
        table = dynamodb.Table(table_name)

        res = table.get_item(
           Key={
               "string":{
                   "email": email,
                   "password": password
               }
           } 
        )
        print(res)

def return_message(mensage, status_code, mensage_key, email):
    return {
            'statusCode': status_code,
            'headers': { 'Content-Type': 'application/json', "Access-Control-Allow-Origin": "*" },
            'body': json.dumps({mensage_key: mensage, "email": email})
        }