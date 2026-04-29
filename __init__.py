from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my_secret_key_2026'
    from .routes import main
    app.register_blueprint(main)
    return app