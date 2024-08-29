# app/app.py
import os
import sys
from flask import Flask, render_template

# Add the parent directory of src to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Assuming create_app is in src/app_factory.py
from src.app_factory import create_app

# Initialize Flask and Dash apps
app = create_app()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
