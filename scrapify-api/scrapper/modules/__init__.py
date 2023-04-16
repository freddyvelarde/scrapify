from flask import Flask
from modules.controllers.scrapping import scrapping_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

CORS(
    app,
    resources={r"/api/*": {"origins": ["http://localhost:3000/"]}},
)

app.register_blueprint(scrapping_bp)
