from boggle import Boggle
from flask import Flask, render_template, session, request, redirect, jsonify

from flask_debugtoolbar import DebugToolbarExtension
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "####"
# the toolbar is only enabled in debug mode:
app.debug = True
toolbar = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route("/")
def show_board():
    """shows main index page with board"""

    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board=board)


@app.route("/check-word", methods=["POST"])
def check_word():
    """checks if user input is valid and redirects back to index page with the response"""

    json_obj = json.loads(request.data)
    guess = json_obj['guess']

    response = {}
    response['result'] = boggle_game.check_valid_word(session['board'], guess)

    redirect('/')

    return jsonify(response)


@app.route("/games-played", methods=["POST"])
def games_played():
    """track how many games have been played"""
    json_obj = json.loads(request.data)

    session['games_played'] = json_obj['games_played']
    response = {}
    response['games_played'] = session['games_played']

    redirect('/')

    return jsonify(response)
