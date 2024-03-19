import os
import logging

# Creating a lightweight webserver using flask to host the API. 
from flask import Flask
from src.ml.factory import ModelFactory

# Setting the project root directory.
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loading the model initially and loading it in flask session memory to avoid re-intialisation on every request.
model_factory = ModelFactory(project_dir=project_dir)

def create_app(flask_config: str = 'development'):
    # Initalize flask app
    flask_app = Flask(__name__)

    # Set Flask configs
    flask_config = flask_config.capitalize()
    flask_app.logger.info(f'Initalizing Flask app for {flask_config} environment...')
    flask_app.config.from_object(f'config.{flask_config}')

    with flask_app.app_context():
        flask_app.static_url_path = flask_app.config.get('STATIC_FOLDER')
        flask_app.config['MODEL_FACTORY'] = model_factory
        flask_app.static_folder = os.path.join(
            flask_app.root_path, flask_app.static_url_path
        )

        from .views import home
        flask_app.register_blueprint(home.bp)
        from .views import demo
        flask_app.register_blueprint(demo.bp)
        flask_app.logger.info(
            f"Initialized Flask app for {flask_config} environment..."
        )
        return flask_app