from flask import Blueprint, jsonify, request
from app.env import access_token
import uuid
import lyricsgenius
import app.aws_controller as aws
import json
import redis
from datetime import datetime


limit=10
bp_app = Blueprint('partitura_endpoint', __name__)
genius = lyricsgenius.Genius(access_token)
redis_con = redis.Redis(host='redis', port=6379, db=0)
# redis_con = redis.Redis(host='localhost', port=6379, db=0)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/musics', methods=['POST'])
def list_music():
    artist = request.args.get('artist')
    cache = request.args.get('cache')
    cache = json.loads(cache.lower())

    resp, status = get_data_from_redis(artist)

    if cache:
        if resp:      
            return jsonify(resp), status
    else:
        delete_data_from_redis(artist)
    try:
        resp, status = get_musics(artist)
    except:
        return jsonify({"error":"No response from GENIUS API"}), 500

    return jsonify(resp), status


def delete_data_from_redis(artist):
    redis_con.delete(artist)
    

def get_data_from_redis(artist):    
    resp = redis_con.get(artist)
    
    if not resp:
        return dict(), 204

    resp = eval(resp.decode("utf-8"))
    return resp, 200


def get_musics(artist):
    
    resp = get_data_from_genius(artist)
    
    try:
        # cria um registro no dynamodb
        aws.put(resp)

        #criar um registro no redis com validade de 7 dias (604800 seg.)
        id = resp['artist']
        redis_con.set(id, json.dumps(resp), ex=604800)

        resp, status = get_data_from_redis(artist)

        return resp, 201
    
    except:
        return {"error":"No response from GENIUS API"}, 500
    

    

def get_data_from_genius(artist):
    data = list()
    try:
        result = genius.search_artist(artist, max_songs=limit, sort='popularity')  
    except:
        resp = {"error":"No response from GENIUS API"}
        return  resp
    
    for song in result.songs:
        data.append(song.title)

    resp = {
        'transaction_id': str(uuid.uuid4()),
        'artist': artist,
        'music': data,
        'created_at': str(datetime.now())    
        }
    
    return resp