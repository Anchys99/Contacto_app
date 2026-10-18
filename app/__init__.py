from flask import Flask
from .routes import routes

def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/static"

    )

    app.config['SECRET_KEY'] = 'clave-secreta'

    # Registrar las rutas
    app.register_blueprint(routes)

    return app