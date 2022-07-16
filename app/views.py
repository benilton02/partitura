from functools import cache
from flask import Blueprint, jsonify, request
from app.env import   access_token
from uuid import uuid4
import lyricsgenius
import app.aws_controller as aws
import json
import redis


limit=3
bp_app = Blueprint('partitura_endpoint', __name__)
genius = lyricsgenius.Genius(access_token)
redis_con = redis.Redis(host='localhost', port=6379, db=0)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/musics', methods=['POST'])
def list_music():
    artist = request.args.get('artist')
    cache = request.args.get('cache')

    if not cache:

        resp, status = get_data_from_redis(artist)
        if not resp:      
            resp, status = get_musics(artist)

        return jsonify(resp), status
    
    resp, status = delete_data_from_redis(artist)
    return jsonify(resp), status



def delete_data_from_redis(artist):
    redis_con.delete(artist)
    resp = {"msg":"Deleted"}
    return resp, 200

@bp_app.route('/delete', methods=['DELETE'])
def delete_data_from_redis():
    artist = request.args.get('artist')
    redis_con.delete(artist)
    resp = {"msg":"Deleted"}
    return resp, 200


def get_data_from_redis(artist):    
    resp = redis_con.get(artist)
    
    if not resp:
        return dict(), 204

    resp = eval(resp.decode("utf-8"))
    return resp, 200


def get_dynamodb():
    artist = request.args.get('artist')
    resp = aws.get(artist)
    return jsonify(resp), 200
    ...


def get_musics(artist):
    
    resp = get_data_from_genius()
    # cria um registro no dynamodb
    aws.put(resp)
    
    #crira um registro no redis com validade de 7 dias (604800 seg.)
    id = resp['artist']
    redis_con.set(id, json.dumps(resp), ex=604800)
    resp, status = get_data_from_redis(artist)
    return resp, 201
    

def get_data_from_genius(artist):
    data = list()
    try:
        result = genius.search_artist(artist, max_songs=limit, sort='popularity')  
    except:
        resp = {"error": "API Genius"}
        return  resp, 500
    
    for song in result.songs:
        data.append(song.title)

    resp = {
        'transaction_id': uuid4().hex,
        'artist': artist,
        'music': data    
        }
    
    return resp