"""Task API - Flask Application Entry Point (exercise variant; video uses Blueprint version)."""
from flask import Flask
from config import Config
from middleware import setup_logging

app = Flask(__name__)
app.config.from_object(Config)
setup_logging(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
