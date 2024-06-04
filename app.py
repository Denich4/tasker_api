from flask import Flask
import sqlite3 as sql
from flask_cors import CORS

from blueprints.task_bp import app_task

app = Flask(__name__)
CORS(app)

app.register_blueprint(app_task)

if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True, host="192.168.0.109")