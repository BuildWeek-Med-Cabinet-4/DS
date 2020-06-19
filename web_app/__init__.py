from flask import Flask
from web_app.routes.result_routes import result_routes


def create_app():
    """Instaniate Flask API application."""
    app = Flask(__name__)
    
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_DATABASE_TRACKING"] = False

    
    app.register_blueprint(result_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

