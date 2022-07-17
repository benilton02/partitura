import os

# Set environment GENIUS API variables
os.environ['CLIENT_ID'] = 'PUT_CLIENT_ID_HERE'
os.environ['CLIENT_SECRET'] = 'PUT_CLIENT_SECRET_HERE'
os.environ['ACCESS_TOKEN'] = 'PUT_ACCESS_TOKEN_HERE'

# Set environment AWS variables
os.environ['ACCESS_KEY_ID'] = 'PUT_ACCESS_KEY_ID_HERE'
os.environ['SECRET_ACCESS_KEY'] = 'PUT_SECRET_ACCESS_KEY_HERE'
os.environ['REGION_NAME']='PUT_REGION_NAME_HERE'

# Get environment GENIUS API variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
access_token = os.getenv('ACCESS_TOKEN')

# Set environment AWS variables
access_key_id = os.getenv('ACCESS_KEY_ID')
secret_access_key = os.getenv('SECRET_ACCESS_KEY')
region_name_aws = os.getenv('REGION_NAME')
