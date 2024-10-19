from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the root directory of the current script
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(root_dir, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
