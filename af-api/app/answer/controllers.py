from flask import Blueprint, request, jsonify
from app import db
from app.answer.models import Answer, answers_schema
from app.question.models import Question, question_schema

answer_mod = Blueprint('answer', __name__)

@answer_mod.route('/question/<question_id>/answers')
def index(question_id):
	all_answers = Answer.query.filter_by(question_id=question_id).all()
	question = Question.query.filter_by(id=question_id).first()

	r_question = question_schema.dump(question)
	r_answers = answers_schema.dump(all_answers)
	return jsonify(answers=r_answers,question=r_question)

@answer_mod.route('/question/<question_id>/answer', methods=["POST"])
def create(question_id):
	content = request.get_json()
	try:
		new_a = Answer(content["answer"], question_id)
		db.session.add(new_a)
		db.session.commit()
		message = "Answer successfully submitted!"
		code = 200
	except:
		message = "Answer could not be submitted. Try agin later."
		code = 401

	return jsonify(message=message), code

@answer_mod.route('/answer/<answer_id>', methods=["PATCH"])
def update(answer_id):
	content = request.get_json()

	try:
		update_a = Answer.query.filter_by(id=answer_id).first()
		update_a.answer = content["answer"]
		update_a.status = "edited"
		db.session.commit()
		message = "Answer successfully updated!"
		code = 200
	except:
		message = "Answer could not be updated. Try agin later."
		code = 401

	return jsonify(message=message), code

@answer_mod.route('/answer/<answer_id>', methods=["DELETE"])
def delete(answer_id):
	try:
		delete_a = Answer.query.filter_by(id=answer_id).first()
		db.session.delete(delete_a)
		db.session.commit()
		message = "Answer successfully deleted. Bye-bye!"
		code = 200
	except:
		message = "Answer could not be deleted. Try agin later."
		code = 401

	return jsonify(message=message), code

@answer_mod.route('/answer/<answer_id>/thumbs_up', methods=["PUT"])
def thumbs_up(answer_id):
	try:
		update_a = Answer.query.filter_by(id=answer_id).first()
		update_a.like_count = update_a.like_count + 1
		db.session.commit()
		message = update_a.like_count
		code = 200
	except:
		message = "Answer could not be upvoted. Try agin later."
		code = 401

	return jsonify(message=message), code

@answer_mod.route('/answer/<answer_id>/thumbs_up', methods=["DELETE"])
def remove_thumbs_up(answer_id):
	try:
		update_a = Answer.query.filter_by(id=answer_id).first()
		update_a.like_count = update_a.like_count - 1
		db.session.commit()
		message = update_a.like_count
		code = 200
	except:
		message = "Answer could not be upvoted. Try agin later."
		code = 401

	return jsonify(message=message), code