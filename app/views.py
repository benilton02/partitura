from flask import Blueprint, jsonify
from app.env import  client_id, client_secret, access_token
from uuid import uuid4
import lyricsgenius


bp_app = Blueprint('partitura_endpoint', __name__)
genius = lyricsgenius.Genius(access_token)

def configure(app):
    app.register_blueprint(bp_app)


@bp_app.route('/list-music/<artist_name>', methods=['GET'])
def list_music(artist_name):
    data = list()
    genius = lyricsgenius.Genius(access_token)
    result = genius.search_artist(artist_name, max_songs=10, sort='popularity')  
    
    for song in result.songs:
        data.append(song.title)

    resp = {
        "transaction": {
            "id": uuid4(),
            "popularity": data
        }
    }

    return  jsonify(resp), 200
