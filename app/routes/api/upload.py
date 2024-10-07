from flask import jsonify, request, abort
import vercel_blob

from app.routes.api import api

# def allowed_file(filename):
#   ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'mp4'}
#   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@api.route('/upload', methods=['POST'])
def upload():
  
  # Get optional filename parameter from the request
  custom_filename = request.form.get('filename', False)
  path = request.form.get('path', False)
  path = f"{path}/" if path else "files/"
  access = request.form.get('access', 'public')
    
  if 'file' not in request.files:
    abort(400, "No file part in request")
  
  file = request.files['file']
    
  if file.filename == '' and not custom_filename:
    abort(400, "No file selected and no custom filename provided")
    
  filename = (custom_filename if custom_filename else file.filename) + '.' + file.filename.split('.')[1]
    
  try:
    response = vercel_blob.put(f"{path}{filename}", file.read(), {
      'access': access,
      'addRandomSuffix': False,
    })
    return jsonify(response), 201
  except Exception as err:
    abort(500, str(err))
