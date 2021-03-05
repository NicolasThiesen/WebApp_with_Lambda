import boto3
import json
import os

def handler(event,context):
    data = json.loads(event["body"])
    dynamodb = boto3.resource("dynamodb")
    if("username" in data) and ("password" in data) and ("email" in data):
        # get the data
        username = data["username"]
        password = data["password"]
        email = data["email"]
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
            return return_message("Itens Inseridos com sucesso!", 200, "status" )
        else:
            return return_message("Algo inesperado aconteceu ao inserir items na tabela", 400, "erro")
    else:
        return return_message("Erro! Parametros insuficientes!", 400, "erro")

def return_message(mensage, status_code, mensage_key):
    return {
            'statusCode': status_code,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({mensage_key: mensage})
        }