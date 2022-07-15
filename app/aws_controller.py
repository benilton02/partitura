import boto3
from app.env import secret_access_key, access_key_id, aws_url

 
dynamodb_client = boto3.client('dynamodb', 
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    # endpoint_url=aws_url
)

table_name = 'Music'
        
def put():
    table = dynamodb_client.list_tables()['TableNames']
    if table:
        # dynamodb_client.get_item(TableName = table_name, Key = data)
        # dynamodb_client.put_item(TableName = table_name, Item = data)
        ...
    print("No Table!")
    
