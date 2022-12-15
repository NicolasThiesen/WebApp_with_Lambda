import boto3
import os
from json import dumps, loads
def handler(event,context):
    print(event)
    dynamodb = boto3.resource("dynamodb")
    body = loads(event["body"])
    if("username" in body) and ("password" in body) and ("email" in body):
        # get the data
        username = body["username"]
        password = body["password"]
        email = body["email"]
        table_name = os.environ["DYNAMO_TABLE"]
        table = dynamodb.Table(table_name)
        res = table.put_item(
            Item={
                "email": email,
                "username": username,
                "password": password
            }
        )
        r_status = int(res["ResponseMetadata"]["HTTPStatusCode"])
        if(r_status == 200):
            return return_message("Itens Inseridos com sucesso!", "status", email , 200)
        else:
            return return_message("Algo inesperado aconteceu ao inserir items na tabela", "erro", "", 400)
    else:
            return return_message("Erro! Parametros insuficientes!", "erro", "" , 400)

def return_message(mensage, mensage_key, email, code):
    return {"statusCode": code, "body": dumps({ mensage_key: mensage,  "email": email})}