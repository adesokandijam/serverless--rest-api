import json
import boto3
import os

table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')
def lambda_handler(event, context):
  data = client.delete_item(
    TableName=table_name,
    Key={
        'id': {
          'N': event['pathParameters']['id']
        }
        }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
    
  return response