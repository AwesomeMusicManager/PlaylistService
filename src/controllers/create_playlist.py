import requests
from flask_restful import Resource, reqparse
from flask import jsonify, request
import logging

class CreatePlaylistWithName(Resource):
    def get(self):
        get_musics = requests.get(
            "https://api.vagalume.com.br/search.excerpt?q={}&limit=5".format(request.args.get('withName')))

        response = []
        for music in get_musics.json()['response']['docs']:
            request.post("https://awesome-music-manager.herokuapp.com/song/new",  )
            response.append({'title': music['title'], 'band': music['band']})

        logging.getLogger().info("VAI PLS")


        return jsonify(response)