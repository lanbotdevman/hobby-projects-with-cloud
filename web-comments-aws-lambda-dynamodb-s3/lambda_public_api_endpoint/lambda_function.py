import boto3
import html
import os
import time
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

# Manually add the environment variable in the Lambda function configuration
table = dynamodb.Table(os.environ['WEB_COMMENTS_TABLE_NAME']) 


def lambda_handler(event, context):

    if 'operation' not in event:
        raise ValueError('Missing operation parameter')

    if event['operation'] == 'getComments':
        return {'status': 'OK', 'comments': read_items()}

    if event['operation'] == 'saveComment' and 'commentText' in event and len(event['commentText']) <= 500:
        add_item(event['commentText'])
        return {'status': 'OK'}

    raise ValueError('Incorrect operation parameter or invalid commentText')


def add_item(commentText):
    print(f'Adding item with text: {commentText}')
    table.put_item(
        Item={
            'id': str('webcomments'),
            'timestamp': int(time.time()),
            'commentText': html.escape(commentText)
        }
    )


def read_items():
    print('Retreiving items')

    response = table.query(
        KeyConditionExpression=Key('id').eq('webcomments')
    )

    return response['Items']