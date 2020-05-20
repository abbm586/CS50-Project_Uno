from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@home_bp.route('/', methods=['GET'])
@home_bp.route('/home', methods=['GET'])
def home():
    return render_template('home.html',
                           title='Flask with Blueprint development',
                           subtitle='Demostration of Flask Web development',
                           template='templates')


@home_bp.route('/default', methods=['GET'])
def default():

    return render_template('default.html',
                           title='Flask with Blueprint development',
                           subtitle='Demostration of Flask Web development')
