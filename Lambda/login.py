import os
import boto3

def handler(event,context):
    dynamodb = boto3.resource("dynamodb")
    if("email" in event) and ("password" in event): 
        email = event["email"]
        password = event["password"]

        table_name = os.environ["DYNAMO_TABLE"]
        table = dynamodb.Table(table_name)

        res = table.get_item(
           Key={
               "email": email
           } 
        )
        item = res["Item"]
        if (item["email"] == email) and (item["password"] == password):
            return return_message("Login Efetuado com sucesso", "status", email)
        else:
            return return_message("Login ou Senha incorretos", "erro", "")
    else:
        return return_message("Login ou Senha incorretos", "erro", "")

def return_message(mensage,  mensage_key, email):
    return {mensage_key: mensage, "email": email}