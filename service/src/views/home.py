from flask import Blueprint
from flask import current_app as app
from flask import render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/', method=['GET'])
def home():
    return render_template('home.html')