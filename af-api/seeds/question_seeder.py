from flask_seeder import Seeder, Faker, generator
from app.question.models import Question

class QuestionSeeder(Seeder):
	def __init__(self, db=None):
		super().__init__(db=db)
		self.priority = 1

	def run(self):
		faker = Faker(
			cls=Question,
			init={
				"question": generator.String('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vitae nulla pretium, euismod neque ut, feugiat est. Curabitur eleifend lacus vel malesuada ornare. Suspendisse volutpat turpis elit, a facilisis orci facilisis sed. Praesent sed nulla non massa tempor tincidunt. Curabitur lobortis ac elit non ullamcorper. Fusce auctor egestas libero. Aliquam vel rutrum tellus. Phasellus ut quam condimentum, tempus tellus vel, faucibus nulla. Duis eu ligula sodales, viverra dolor at, tincidunt elit. Nunc ut pharetra tellus, sit amet euismod quam. Suspendisse aliquet ligula fermentum, suscipit lacus vitae, imperdiet est. In consectetur lacus at dignissim facilisis.'),
				"like_count": generator.Integer(start=0, end=100)
			}
		)

		for question in faker.create(20):
			print("Adding question: %s" % question)
			self.db.session.add(question)