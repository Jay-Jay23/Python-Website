from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/Login')
def login():
    return "<p>Login</p>"


@auth.route('/Logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/Signup')
def signup():
    return "Sign-up"
