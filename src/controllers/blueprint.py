from flask import Blueprint
from flask_restful import Api
from .create_playlist import CreatePlaylistWithName


def setup_blueprint():
    blueprint = Blueprint(
        "playlist", __name__,
    )

    api = Api(blueprint)
    api.add_resource(CreatePlaylistWithName, '/api/v1/create-playlist')
    return blueprint