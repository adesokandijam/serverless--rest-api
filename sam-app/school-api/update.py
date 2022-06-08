import json
import boto3
import os

table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')
def lambda_handler(event, context):
  try:
    data = client.update_item(
      TableName=table_name,
      Key={
        'id': {
          'N': event['pathParameters']['id']
        }
      },
      UpdateExpression="set department = :value",
      ExpressionAttributeValues={
        ":value": {'S': event['queryStringParameters']['department']}
      },
      ReturnValues= "UPDATED_NEW"
    )

    response = {
      'statusCode': 200,
      'body': "updated field department successfully",
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }
    
  except ClientError as e:
    logger.error(e.response['Error']['Message'])
    raise
  else:
    return response