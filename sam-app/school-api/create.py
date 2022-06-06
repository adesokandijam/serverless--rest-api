import json
import boto3
import os
import uuid


# import requests
table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    data = client.put_item(
        TableName = table_name,
        Item={
            'id': {
                'N': event['queryStringParameters']['id'] 
            },
            "name": {
                'S': event['queryStringParameters']['name'] 
            },
            'matric_no': {
                'S': event['queryStringParameters']['matric_no'] 
            },
            'department': {
                'S': event['queryStringParameters']['department'] 
            },
            'faculty': {
                'S': event['queryStringParameters']['faculty'] 
            },
            'CGPA': {
                'S': event['queryStringParameters']['CGPA'] 
            },
            'year_of_grad': {
                'S': event['queryStringParameters']['grad_year'] 
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

    return response