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
    # Write code here
    # return render_template("index.html")
    return "Hello"


@app.route("/questionnaireMBTI")
def questionnaire():
    MBTI_questions = ["a", "b", "c", "d"]
    if request.method == "GET":
        return render_template("questionnaireMBTI.html", MBTI_questions = MBTI_questions)
    # add else statement if method == 'post' and return value of the personality type etc.


if __name__ == "__main__":
    app.run()
