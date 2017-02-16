from combact import Combat
import random

class Character(Combat):
	attack_limit = 10
	experience  = 0
	base_hit_points = 10

	def attack(self):
		roll = random.randint(1,self.attack_limit)

		if self.weapon == 'sword':
			roll += 1

		elif self.weapon == 'axe':
			roll += 2


		return roll > 4

	def get_weapon(self):
		wep = input("Choose Your Weapon.([S]word , [A]xe , [B]ow)").lower()

		if wep in 'sab':
			if wep == 's':
				return 'sword'
			elif wep == 'a':
				return 'axe'
			else:
				return 'Bow'

		else:
			print("Weapon not in you arsenal right now")
			return self.get_weapon()
	


	def __init__(self,**kwargs):
		self.name = input("Enter Name:")
		self.weapon = self.get_weapon()
		self.hit_points = self.base_hit_points

		for key,value in kwargs.items():
			setattr(self,key,value)

	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name,self.hit_points,self.experience)

	def rest(self):
		if self.hit_points < self.base_hit_points:
			self.hit_points += 1

	def  level_up(self):
		return self.experience > 5
