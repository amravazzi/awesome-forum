from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

seeder = FlaskSeeder(app, db)

ma = Marshmallow(app)

# 404 error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify(error='Resource not found.'), 404

from app.question.controllers import question_mod as question
app.register_blueprint(question)

from app.answer.controllers import answer_mod as answer
app.register_blueprint(answer)