from flask import Flask
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    # Registra o blueprint que contém todas as rotas
    app.register_blueprint(main_bp)

    return app
