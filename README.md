# partitura

### Dependencies
- Python ^3.9
- Docker
- Docker compose

### Environment variables
###### Inside app/env.py file 
GENIUS API variables
```sh
os.environ['CLIENT_ID'] = 'DEFINES_CLIENT_ID_HERE'
os.environ['CLIENT_SECRET'] = 'DEFINES_CLIENT_SECRET_HERE'
os.environ['ACCESS_TOKEN'] = 'DEFINES_ACCESS_TOKEN_HERE'
```

AWS variables
```sh
os.environ['ACCESS_KEY_ID'] = 'DEFINES_ACCESS_KEY_ID_HERE'
os.environ['SECRET_ACCESS_KEY'] = 'DEFINES_SECRET_ACCESS_KEY_HERE'
os.environ['REGION_NAME']='DEFINES_REGION_NAME_HERE''

```

### How to run in docker
Run application
```sh
docker-compose up --build

```