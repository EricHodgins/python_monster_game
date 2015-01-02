#In python 3 we don't have to inlcude the inheritance chain for basic classes.
#attributes don't need to use the parantheses () b/c they're not methods.
#methods are functions in Classes.  Functions are stand alone.
# remember ** is for unpacking dictionaries usually, and * is for unpacking tuples
# setattr(x, 'foobar', 123) = x.foobar = 123

import random
from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

	def __init__(self, **kwargs):
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)  #-> self.key = value

	def __str__(self):
		return "{} {}, HP: {}, XP:{}".format(self.color.title(),
											  self.__class__.__name__,
											  self.hit_points,
											  self.experience)


	def battlecry(self):
		return self.sound.upper()


class Goblin(Monster):
	max_hit_points = 3
	max_experience = 2
	sound = 'squeak'

class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound = 'growl'

class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound = 'raaaaaaaar'