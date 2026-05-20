from flask import Flask
import pandas as pd
import numpy as np

# Create Flask app instance
app = Flask(__name__)

# Define route
@app.route('/')
def home():
    return "Hello, World! Welcome to Flask."

# Run application
if __name__ == '__main__':
    app.run(debug=True)