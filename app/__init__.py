import os
from flask import Flask
from flask_cors import CORS

def create_app():
    application = Flask(__name__)
    #CONFIG_TYPE = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    #application.config.from_object(CONFIG_TYPE)

    CORS(application, origins=["http://localhost:3000"])

    #from db import db

    #db.init_app(application)
    #migrate = Migrate(application, db)
    #flask_api = Api(application)


    #from app.routes.characters import blp as CharacterBlueprint
    #from app.routes.users import blp as UserBlueprint

    #flask_api.register_blueprint(CharacterBlueprint)
    #flask_api.register_blueprint(UserBlueprint)

    @application.route("/", methods=["GET"])
    def hello_world():
        return "Hola mundo", 200
    
    @application.route("/api/testing_server", methods=["GET"])
    def testing_server():
        return "ok", 200

    return application


