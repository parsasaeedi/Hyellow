from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# from helpers import apology, login_required

import requests
import urllib.parse
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#  Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///speedtyping.db")


# Index
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")


# signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['confirm_password']:
            error = 'Password does not match!'
        else:
            return redirect(url_for('index'))
    return render_template('signup.html', error=error)


# MBTI
@app.route("/questionnaire/1")
def MBTI():
    MBTI_questions = [
        "After a tiring weekend you recharge by being with people instead of being by yourself",
        "Instead of thinking about present details, you'd rather think of future possibilities",
        "You analyze the problem to make decisions instead of just trusting your gut",
        "You'd rather plan your birthday compared to celebrating it spontaneously"]
    test = "MBTI"
    if request.method == "GET":
        return render_template("questionnaireMBTI.html", questions = MBTI_questions, test = test)
    # add else statement if method == 'post' and return value of the personality type etc.


# acouplemorethings
@app.route("/acouplemorethings")
def acouplemorethings():
    return render_template("acouplemorethings.html")


# seehowitworks
@app.route("/seehowitworks")
def seehowitworks():
    return render_template("seehowitworks.html")


if __name__ == "__main__":
    app.run()
