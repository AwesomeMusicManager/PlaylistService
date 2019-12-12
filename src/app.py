from flask import Flask
from flask_restful import Resource, Api
from controllers.blueprint import setup_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from pygelf import GelfUdpHandler
import logging
from cmreslogging.handlers import CMRESHandler


handler = CMRESHandler(hosts=[{'host': 'docker-elk_logstash_1', 'port': 5000}],
                           auth_type=CMRESHandler.AuthType.NO_AUTH,
                           es_index_name="my_python_index")
log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(handler)
log.info('go!')

app = Flask(__name__)
api = Api(app)

app = Flask(__name__, static_url_path='/static')

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(setup_blueprint())

if __name__ == '__main__':
    app.run(debug=True, port=4500)