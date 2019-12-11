from flask import Flask
from flask_restful import Resource, Api
from controllers.create_playlist import CreatePlaylistWithName

app = Flask(__name__)
api = Api(app)

api.add_resource(CreatePlaylistWithName, '/api/v1/create-playlist')

if __name__ == '__main__':
    app.run(debug=True)