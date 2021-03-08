import boto3
import os

def handler(event, context):
    sns_arn = os.environ["SNS_ARN"]
    table_name = os.environ["DYNAMO_TABLE"]
    email = event["email"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    sns = boto3.client("sns",region_name="us-east-1")
    res = sns.subscribe(TopicArn=sns_arn,Protocol="Email",Endpoint=email, ReturnSubscriptionArn=True)
    res_dynamo = table.put_item(
            Item={
                "email": email,
                "SubscriptionArn": res["SubscriptionArn"],
                "Confirmed": False
            }
        )
    if ( res_dynamo["ResponseMetadata"]["HTTPStatusCode"] == 200) and ( res["ResponseMetadata"]["HTTPStatusCode"] == 200):
        return {"Status": "A subscrição foi feita, confirmação pendente."}
    else:
        return {"Status": "Algo de errado aconteceu ao subeescrever o item."}