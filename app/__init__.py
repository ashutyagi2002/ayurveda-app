from flask import Flask
from flask_mysql_connector import MySQL
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from dotenv import load_dotenv

mysql = MySQL()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Secret key & DB Config
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "defaultsecret")
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST", "localhost")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER", "root")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD", "")
    app.config['MYSQL_DATABASE'] = os.getenv("MYSQL_DATABASE", "ayurveda_db")

    mysql.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Blueprints import
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
