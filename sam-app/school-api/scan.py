import json
import boto3
import os

table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')
def lambda_handler(event, context):
  data = client.scan(
    TableName=table_name
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return {response['Items']}