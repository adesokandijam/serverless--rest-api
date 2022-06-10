import json
import boto3
import os
import uuid


# import requests
table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    try: 
        data = client.put_item(
            TableName = table_name,
            Item={
                'id': {
                'N': body['id'] 
                },
                "name": {
                    'S': body['name'] 
                },
                'matric_no': {
                    'S': body['matric_no'] 
                },
                'department': {
                    'S': body['department'] 
                },
                'faculty': {
                    'S': body['faculty'] 
                },
                'CGPA': {
                    'S': body['CGPA'] 
                },
                'year_of_grad': {
                    'S': body['grad_year'] 
                }
            }
        )
    
        response = {
        'statusCode': 200,
        'body': 'successfully created item!',
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