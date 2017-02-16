import random

COLOR = ['blue', 'red', 'green', 'yellow']


class Monsters:
	max_hitpoints = 1
	min_hitpoints = 1
	max_experience = 1
	min_experience = 1
	weapon='sword'
	sound = 'roar'
	def __init__(self, **kwargs):
		self.hit_points = random.randint(self.min_hitpoints,self.max_hitpoints)
		self.color = random.choice(COLOR)
		self.experience = random.randint(self.min_experience,self.max_experience)

		for key,value in kwargs.items():
			setattr(self,key,value)

	def __str__(self):
		return '{} {} HP: {} XP: {}'.format(self.color.title(),self.__class__.__name__,self.hit_points,self.experience)


	def battlecry(self):
		return self.sound.upper()

	def  say_color(self):
		return self.color.upper()

	def test(self):
		roll = random.randint(1,4)
		return roll > 4

class Goblin(Monsters):
	max_experience=2
	min_hitpoints = 2
	max_hitpoints = 3

	sound = 'Squek'

class Troll(Monsters):
	max_experience = 5
	min_experience = 2
	max_hitpoints = 8
	min_hitpoints = 5

	sound = 'Wiggling'

class Dragon(Monsters):
	max_hitpoints = 10
	min_hitpoints = 7
	max_experience = 10
	min_experience = 8

	weapon = 'fire'
	sound = 'raaaaaaar'