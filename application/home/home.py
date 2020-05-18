from flask import Flask, Blueprint, render_template

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@home_bp.route('/', methods=['GET'])
def home():
    return '<h2>Home Page</h2>'
    # return render_template('home.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')


@home_bp.route('/default', methods=['GET'])
def default():
    return '<h2>Default Page</h2>'
    # return render_template('.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')
