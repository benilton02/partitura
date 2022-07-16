import boto3
from app.env import secret_access_key, access_key_id, region_name_aws 


client = boto3.client(
    'dynamodb', 
    region_name=region_name_aws,
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
                {
                    'AttributeName': 'transaction_id',
                    'KeyType': 'RANGE' 
                },
        
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'artist',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'transaction_id',
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
                'SS': input['music']
            },
            'created_at' : {
                'S': input["created_at"]
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
    

    