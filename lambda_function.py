import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserMessages')

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    # Handle CORS preflight OPTIONS request
    method = event.get('requestContext', {}).get('http', {}).get('method', '')
    if method == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}
        
    body = json.loads(event.get('body') or '{}')
    name = body.get('name', 'Anonymous')
    message = body.get('message', '')
    
    table.put_item(
        Item={
            'id': str(uuid.uuid4()),
            'name': name,
            'message': message
        }
    )
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({'status': 'Message saved successfully!'})
    }
