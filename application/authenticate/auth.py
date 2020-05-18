from flask import Flask, Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route('/login', methods=['POST'])
def login():
    return '<h2>Login Page</h2>'
    # return render_template('login.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')


@auth_bp.route('/register', methods=['POST'])
def register():
    return '<h2> Register Page </h2>'
    # return render_template('register.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')
