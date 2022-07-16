from functools import cache
from flask import Blueprint, jsonify, request
from app.env import   access_token
from uuid import uuid4
import lyricsgenius
import app.aws_controller as aws


limit=2
bp_app = Blueprint('partitura_endpoint', __name__)
genius = lyricsgenius.Genius(access_token)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/musics', methods=['POST'])
def list_music():
    data = list()
    artist = request.args.get('artist')
    cache = request.args.get('cache') #se não informado retorna None
    try:
        result = genius.search_artist(artist, max_songs=limit, sort='popularity')  
    except:
        resp = {"error": "API Genius"}
        return  jsonify(resp), 500
    
    for song in result.songs:
        data.append(song.title)

    resp = {
        'transaction_id': uuid4().hex,
        'artist': artist,
        'music': data
        }
    
    aws.put(resp)
    return  jsonify(resp), 200

