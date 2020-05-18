from flask import Flask, Blueprint, render_template

view_bp = Blueprint('view_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@view_bp.route('/list', methods=['GET'])
def list():
    return '<h2>Book list Page</h2>'
    # return render_template('list_all.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')


@view_bp.route('/search', methods=['GET'])
def search():
    return '<h2>Search Results Page</h2>'
    # return render_template('.html',
    #                        title='Flask with Blueprint development',
    #                        subtitle='Demostration of Flask Web development')
