import os
from src import app

from flask import request, redirect, flash
from werkzeug import secure_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in os.getenv('ALLOWED_EXTENSIONS')

def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file submitted', 'warning')

    file = request.files['file']

    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file', 'danger')

    if file and allowed_file(file.filename):
         file.save(secure_filename(file.filename))
         print('Upload Competed Successfully')
         return 'success'
