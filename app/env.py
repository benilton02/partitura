import os

# Set environment GENIUS API variables
os.environ['CLIENT_ID'] = '3jNdL2XOru9orzsFoPiSL6lILAUYPkcRAi1e7AOfwePzkCWj7FDGO4g7p3XjXEr3'
os.environ['CLIENT_SECRET'] = 'ZHmP29rn3M79dugOmZDsJtr7wPxUTId6_s7ULSWsMviHUVL2TNwmkjguQflWUvGarjAdyde49n_r9GL-_S-BBw'
os.environ['ACCESS_TOKEN'] = '7lMxyGzINLkTON4PlCt4RPx0s8IJd35DCIICNlJVdnO8SdiZVRSjzTqvSaHb7Jdl'

# Set environment AWS variables
os.environ['ACCESS_KEY_ID'] = 'AKIAZHVWYLSKZQXGCZOB'
os.environ['SECRET_ACCESS_KEY'] = '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'
os.environ['REGION_NAME']='us-east-1'

# Get environment GENIUS API variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
access_token = os.getenv('ACCESS_TOKEN')

# Set environment AWS variables
access_key_id = os.getenv('ACCESS_KEY_ID')
secret_access_key = os.getenv('SECRET_ACCESS_KEY')
region_name_aws = os.getenv('REGION_NAME')
