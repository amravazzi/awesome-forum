from app import db, ma
from app.answer.models import Answer

class Question(db.Model):
	__tablename__ = "questions"

	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.Text(), nullable=False)
	like_count = db.Column(db.Integer(), default=0, nullable=False)
	status = db.Column(db.String(128), default="active", nullable=False)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
	answers = db.relationship('Answer', backref='answers', lazy=True, cascade="all,delete")

	def __repr__(self):
		return '<Question {}>'.format(self.question)

	def __init__(self, question, like_count):
		self.question = question
		self.like_count = like_count

class QuestionSchema(ma.Schema):
	class Meta:
		model = Question
		fields = ("question", "like_count", "status", "updated_at")

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)