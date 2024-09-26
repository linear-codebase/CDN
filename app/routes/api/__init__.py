from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

import app.routes.api.auth

import app.routes.api.upload