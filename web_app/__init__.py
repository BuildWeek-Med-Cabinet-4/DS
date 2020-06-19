
import os
from dotenv import load_dotenv
from flask import Flask
from web_app.routes.result_routes import result_routes
from web_app.routes.from_back_routes import from_back_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def create_app():
    """Instaniate Flask API application."""
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_DATABASE_TRACKING"] = False

    
    app.register_blueprint(result_routes)
    app.register_blueprint(from_back_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

