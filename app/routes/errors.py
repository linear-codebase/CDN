from flask import json
from app import app
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
  response = e.get_response()

  # if e.code == 404:
  #   return redirect('/404-not-found')

  # replace the body with JSON
  response.data = json.dumps({
    "error": {
      "code": e.code,
      "name": e.name.upper(),
      "details": e.description
    }
  })
  response.content_type = "application/json"
  return response