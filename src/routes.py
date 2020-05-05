from flask import Flask, request, render_template
from src.forms import *
from src.file_upload import *
from src import app


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    forms = UserLogin()

    return render_template('login.html', title='login', forms = forms)


@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = UserRegister()

    return render_template('login.html', title='register', forms = forms)


@app.route('/reset', methods=['POST', 'GET'])
def reset():
    forms = PasswordReset()

    return render_template('login.html', title='reset', forms = forms)

#   ===============================================
#       The Route for File Uploading    
#   ===============================================
@app.route('/upload')
def upload():
    return render_template('upload.html', title='File upload')


@app.route('/update', methods=['POST', 'GET'])
def uploaded():
    if request.method == 'POST':
        print(' ======== Uploading started ========')
        if 'file' not in request.files:
            flash('No file submitted', 'warning')

        file = request.files['file']

        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')

        if file and allowed_file(file.filename):
            file.save(secure_filename(file.filename))
            print('Upload Completed Successfully')
            status = True
            flash('File Upload was successful', 'success')
            # return redirect('update.html')
            return 'success'