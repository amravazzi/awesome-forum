from flask import Blueprint, request, jsonify
from app import db
from app.question.models import Question, questions_schema, question_schema

question_mod = Blueprint('question', __name__)

@question_mod.route('/questions')
def index():
	all = Question.query.all()
	result = questions_schema.dump(all)
	return jsonify(questions=result)

@question_mod.route('/question', methods=["POST"])
def create():
	content = request.get_json()
	try:
		new_q = Question(content["question"])
		db.session.add(new_q)
		db.session.commit()
		message = "Question successfully submitted!"
		code = 200
	except:
		message = "Question could not be submitted. Try agin later."
		code = 401

	return jsonify(message=message), code

@question_mod.route('/question/<question_id>', methods=["PATCH"])
def update(question_id):
	content = request.get_json()

	try:
		update_q = Question.query.filter_by(id=question_id).first()
		update_q.question = content["question"]
		update_q.status = "edited"
		db.session.commit()
		message = "Question successfully updated!"
		code = 200
	except:
		message = "Question could not be updated. Try agin later."
		code = 401

	return jsonify(message=message), code

@question_mod.route('/question/<question_id>', methods=["DELETE"])
def delete(question_id):
	try:
		delete_q = Question.query.filter_by(id=question_id).first()
		db.session.delete(delete_q)
		db.session.commit()
		message = "Question successfully deleted. Bye-bye!"
		code = 200
	# except Exception as err:
	# 	return f"{err.__class__.__name__}: {err}"
	except:
		message = "Question could not be deleted. Try agin later."
		code = 401

	return jsonify(message=message), code

@question_mod.route('/question/<question_id>/thumbs_up', methods=["PUT"])
def thumbs_up(question_id):
	try:
		update_q = Question.query.filter_by(id=question_id).first()
		update_q.like_count = update_q.like_count + 1
		db.session.commit()
		message = update_q.like_count
		code = 200
	except:
		message = "Question could not be upvoted. Try agin later."
		code = 401

	return jsonify(message=message), code

@question_mod.route('/question/<question_id>/thumbs_up', methods=["DELETE"])
def remove_thumbs_up(question_id):
	try:
		update_q = Question.query.filter_by(id=question_id).first()
		update_q.like_count = update_q.like_count - 1
		db.session.commit()
		message = update_q.like_count
		code = 200
	except:
		message = "Question could not be downvoted. Try agin later."
		code = 401

	return jsonify(message=message), code