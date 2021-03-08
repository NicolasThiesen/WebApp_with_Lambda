import boto3
import os

def handler(event, context):
    sns_arn = os.environ["SNS_ARN"]

    sub = event["subject"]
    message = event["message"]

    sns = boto3.client("sns",region_name="us-east-1")

    res = sns.publish(
        TopicArn=sns_arn,
        Message=message,
        Subject=sub
    )
    return {"Status": "Mensagem enviada com sucesso"}