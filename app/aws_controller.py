import logging
import boto3
from boto3.dynamodb.conditions import Key
from app.env import secret_access_key, access_key_id 

client = boto3.client(
    'dynamodb', 
    region_name='us-east-1',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key)

    
def create_table():
    table = table_name()
    if not table:
        client.create_table(
                TableName='Music',
            KeySchema=[
                {
                    'AttributeName': 'transaction_id',
                    'KeyType': 'HASH' 
                },
                {
                    'AttributeName': 'artist',
                    'KeyType': 'RANGE' 
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'transaction_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'artist',
                    'AttributeType': 'S' 
                },
            ],
            BillingMode='PAY_PER_REQUEST',
        )
    
def table_name():
    try:
        name = client.list_tables()['TableNames'][0]
    
    except:
        name = str()
    
    finally:
        print(f'TableName: {name}')
        return name
    

def put(input):
    name = table_name()

    client.put_item(
        TableName=name,
        Item={
            'transaction_id': {
                'S': input.get('transaction_id')
            },
            'artist':{
                'S': input.get('artist')
            },
            'music':{
                'S': ". ".join(input.get('music'))
            }
        }
    )

    

            
        
# def get():
#     name = table_name()
#     client.get_item(
#         TableName=name,
#         Key={
#             'transaction_id': {
#                 'S': '5d85e65951e0441a9e57130d418af0ec'
#             }
#         }
        
#     )
#     return client.query(
#         KeyConditionExpression=Key('transaction_id').eq('5d85e65951e0441a9e57130d418af0ec')
#     )

#     ...
    