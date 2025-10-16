from flask import Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "Login Page"

@auth_bp.route('/register')
def register():
    return "Register Page"

@auth_bp.route('/logout')
def logout():
    return "Logout Page"