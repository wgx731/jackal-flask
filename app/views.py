from flask import render_template
from app.models import User, Stock, get_sample_user, get_sample_stocks
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = get_sample_user()
    stocks = get_sample_stocks()
    return render_template("index.html",
                           title='Home',
                           user=user,
                           stocks=stocks)

