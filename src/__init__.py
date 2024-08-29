# src/__init__.py
#from dash import dcc, html
# src/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Additional setup (like configurations, blueprints, etc.)
    
    return app
