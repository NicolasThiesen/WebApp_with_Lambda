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
               "email": email
           } 
        )
        item = res["Item"]
        print(return_message("Login Efetuado com sucesso", 200, "status", email))
        if (item["email"] == email) and (item["password"] == password):
            return return_message("Login Efetuado com sucesso", 200, "status", email)
        else:
            return return_message("Login ou Senha incorretos", 400, "erro", "")

def return_message(mensage, status_code, mensage_key, email):
    return {
            'statusCode': status_code,
            'headers': { 'Content-Type': 'application/json', "Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods': 'POST', 'Access-Control-Allow-Headers': 'Content-Type, X-API-KEY', },
            'body': json.dumps({mensage_key: mensage, "email": email})
        }