from character import Character
from monster import Monsters
from monster import Goblin
from monster import Troll
from monster import Dragon
import sys
import os



class Game:
	def  setup(self):
		self.player = Character()
		self.monsters = [
		Goblin(),
		Troll(),
		Dragon()
		]

	def  get_next_monster(self):
		try :
			return self.monsters.pop(0)

		except IndexError:
			return None

	def clear(self):
		if 	os.name == 'nt':
			os.system('cls')

		else :
			os.system('clear')

	def monster_turn(self):
		if self.monster.attack():
			print('{} is Attacking\n'.format(self.monster))

			if input('Dodge Y/n?').lower() == 'y':
				if self.player.dodge():
					print('You Dodged')

				else:
					print('You could not dodge!!!\n')
					self.player.hit_points -= 1

			else:
				print('{} Attacked you for 1 hitpoint\n'.format(self.monster))

		else:
			print('{} is not attacking this turn\n'.format(self.monster))


	def player_turn(self):
		player_choice = input('You want to [A]ttack , [R]est or [E]xit\n').lower()

		if player_choice == 'a':
			if self.player.attack():
				print('You are Attacking')

				if self.monster.dodge():
					print('{} Dodged Anyway!!\n'.format(self.monster))

				else:
					print('You hit {} for 1 HP\n'.format(self.monster))

					if self.player.level_up():
						self.monster.hit_points -= 2

					else:
						self.monster.hit_points -= 1

			else:
				print('You missed the Attack\n')

		elif player_choice == 'r':
			self.player.rest()

		else:
			sys.exit()

	def cleanup(self):
		#print('*******{}HP in clean ip*********\n'.format(self.monster.hit_points))
		if self.monster.hit_points <= 0:
			self.player.experience = self.monster.experience
			print('You Killed {}\n'.format(self.monster))
			self.monster = self.get_next_monster()


	def  __init__(self):
		self.setup()
		self.monster  = self.get_next_monster()
		while  self.player.hit_points and (self.monster or self.monsters):
			#self.clear()
			print('\n'+'='*20)
			print(self.player)
			print(self.monster)
			self.player_turn()
			self.monster_turn()
			print('\n'+'-'*20)
			self.cleanup()
			


		if self.player.hit_points:
			print('You Win')

		elif self.monster or self.monsters:
			print('You Lose')
			
		sys.exit()

Game()