import boto3
import os
from json import dumps, loads
def handler(event, context):
    print(event)
    sns_arn = os.environ["SNS_ARN"]
    table_name = os.environ["DYNAMO_TABLE"]
    email = loads(event["body"])["email"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    sns = boto3.client("sns",region_name="us-east-1")
    res = sns.subscribe(TopicArn=sns_arn,Protocol="Email",Endpoint=email, ReturnSubscriptionArn=True)
    res_dynamo = table.update_item(
        Key={
            "email": email
        },
        UpdateExpression="set SubscriptionArn=:s, Confirmed=:c",
        ExpressionAttributeValues={
            ":s": res["SubscriptionArn"],
            ":c": False
        },
        ReturnValues="NONE"
    )
    if ( res_dynamo["ResponseMetadata"]["HTTPStatusCode"] == 200) and ( res["ResponseMetadata"]["HTTPStatusCode"] == 200):
        return {
            "statusCode": 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            "body": dumps({"Status": "A subscrição foi feita, confirmação pendente."})}
    else:
        return {"statusCode":400, "body": dumps({"Status": "Algo de errado aconteceu ao subeescrever o item."})}