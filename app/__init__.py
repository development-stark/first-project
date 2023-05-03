import os
from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig
def create_app():
    application = Flask(__name__, static_folder="static", template_folder="templates")
    
    try:
        if os.getenv("ENVIRONMENT") == "development":
            configuration = DevelopmentConfig
        else:
            configuration = ProductionConfig
    except:
        print("there was an error in the configuration")
        raise Exception
        
    application.config.from_object(configuration)
    print(f"Configuration {application.config['FLASK_ENV']}")
    print(application.config['DEBUG'])

    CORS(application, origins=["http://localhost:3000"])

    from db import db

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


