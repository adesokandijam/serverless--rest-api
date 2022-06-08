import json
import boto3
import os

table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')
def lambda_handler(event, context):
  try: 
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
      'body': "deleted successfully",
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