from flask_seeder import Seeder, Faker, generator
from app.answer.models import Answer

class AnswerSeeder(Seeder):
	def __init__(self, db=None):
		super().__init__(db=db)
		self.priority = 2

	def run(self):
		faker = Faker(
			cls=Answer,
			init={
				"answer": generator.String('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vitae nulla pretium, euismod neque ut, feugiat est. Curabitur eleifend lacus vel malesuada ornare. Suspendisse volutpat turpis elit, a facilisis orci facilisis sed. Praesent sed nulla non massa tempor tincidunt. Curabitur lobortis ac elit non ullamcorper. Fusce auctor egestas libero. Aliquam vel rutrum tellus. Phasellus ut quam condimentum, tempus tellus vel, faucibus nulla. Duis eu ligula sodales, viverra dolor at, tincidunt elit. Nunc ut pharetra tellus, sit amet euismod quam. Suspendisse aliquet ligula fermentum, suscipit lacus vitae, imperdiet est. In consectetur lacus at dignissim facilisis.'),
				"question_id": generator.Integer(start=1, end=20),
				"like_count": generator.Integer(start=0, end=100)
			}
		)

		for answer in faker.create(150):
			print("Adding answer: %s" % answer)
			self.db.session.add(answer)