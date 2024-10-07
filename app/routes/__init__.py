from datetime import datetime
import os
from flask import render_template, send_from_directory, Response
import requests
from app import app
from app.routes.api import api
import config

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
  current_year = datetime.now().year

  return render_template('index.html', current_year=current_year)

@app.route('/<path:url_path>')
def proxy_resource(url_path):
  vercel_url = f"{config.URL_VERCEL_STORAGE}/{url_path}"
    
  response = requests.get(vercel_url)

  if response.status_code == 200:
    return Response(response.content, content_type=response.headers['Content-Type'])
  else:
    return f"Erro ao buscar o recurso: {response.status_code}", response.status_code


from app.routes import errors
# Register Blueprints (routes)
app.register_blueprint(api)