import os
from flask import Flask
from flask_bootstrap import Bootstrap



def create_app():
    app = Flask(__name__)

    

    app.config["SECRET_KEY"] = os.environ['SECRET_KEY']
    

    Bootstrap(app)

    # IMPORT MAIN BLUEPRINT AND REGISTER
    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app