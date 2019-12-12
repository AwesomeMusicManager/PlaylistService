import requests
from flask_restful import Resource, reqparse
from flask import jsonify, request

class CreatePlaylistWithName(Resource):
    def get(self):
        get_musics = requests.get(
            "https://api.vagalume.com.br/search.excerpt?q={}&limit=5".format(request.args.get('withName')))

        response = []
        for music in get_musics.json()['response']['docs']:
            response.append({'title': music['title'], 'band': music['band']})

        return jsonify(response)