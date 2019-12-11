from urllib import request
from flask_restful import Resource, reqparse
from flask import jsonify

class CreatePlaylistWithName(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("withName", type=str, required=True)
        args = parser.parse_args()

        # get_musics = request.get("apirubao/args['withName']")
        get_musics = [{"name": "Even Flow"}, {"name": "bellyache"}, {"name": "Madness"}]
        return jsonify(get_musics)