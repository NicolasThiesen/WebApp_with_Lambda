import boto3
import json
import os

def handler(event,context):
    dynamodb = boto3.resource("dynamodb")
    if("username" in event) and ("password" in event) and ("email" in event):
        # get the data
        username = event["username"]
        password = event["password"]
        email = event["email"]
        table_name = os.environ["DYNAMO_TABLE"]
        table = dynamodb.Table(table_name)
        res = table.put_item(
            Item={
                "email": email,
                "username": username,
                "password": password,
                "SubscriptionArn": "",
                "Confirmed": ""

            }
        )
        r_status = int(res["ResponseMetadata"]["HTTPStatusCode"])
        if(r_status == 200):
            return return_message("Itens Inseridos com sucesso!", "status", email )
        else:
            return return_message("Algo inesperado aconteceu ao inserir items na tabela", "erro", "")
    else:
            return return_message("Erro! Parametros insuficientes!", "erro", "" )

def return_message(mensage, mensage_key, email):
    return {mensage_key: mensage,  "email": email}