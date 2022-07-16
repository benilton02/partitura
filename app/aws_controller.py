from ast import Str
import logging
import boto3
from app.env import secret_access_key, access_key_id 
from datetime import datetime

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
                    'AttributeName': 'artist',
                    'KeyType': 'HASH' 
                },
        
            ],
            AttributeDefinitions=[
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
                'S': input['transaction_id']
            },
            'artist':{
                'S': input['artist']
            },
            'music':{
                # 'S': ". ".join(input.get('music'))
                'SS': input['music']
            },
            'created_at' : {
                'S': str(datetime.now())
            }
        }
    )
  
        
def get(artist):
    name = table_name()
    return client.get_item(
        TableName=name,
        Key={
            'artist': {'S': artist},
        }
    )
    

    