from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os



db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'


    from . import models

    from .auth import  auth_bp
    from .expenses import expenses_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)

    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app

