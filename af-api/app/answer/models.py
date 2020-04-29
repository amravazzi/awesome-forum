from app import db, ma

class Answer(db.Model):
	__tablename__ = "answers"

	id = db.Column(db.Integer, primary_key=True)
	answer = db.Column(db.Text(), nullable=False)
	question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
	like_count = db.Column(db.Integer(), default=0, nullable=False)
	status = db.Column(db.String(128), default="active", nullable=False)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

	def __repr__(self):
		return '<Answer {}>'.format(self.answer)

	def __init__(self, answer, question_id, like_count):
		self.answer = answer
		self.question_id = question_id
		self.like_count = like_count

class AnswerSchema(ma.Schema):
	class Meta:
		model = Answer
		fields = ("id", "answer", "question_id", "like_count", "status", "updated_at")

answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)