from . import main
from flask import current_app, render_template

@main.route('/')
def home():
    return render_template('main/home.html')

@main.route('/wallet')
def wallet():
    return render_template('main/home.html')

@main.route('/game')
def game():
    return render_template('main/home.html')

@main.route('/leaderboard')
def leaderboard():
    return render_template('main/home.html')
