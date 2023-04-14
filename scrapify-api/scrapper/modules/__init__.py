from flask import Flask
from modules.controllers.scrapping import scrapping_bp

app = Flask(__name__)

app.register_blueprint(scrapping_bp)
