import random
import os
import sys

fruits = [
    'apple',
    'mango',
    'grapes',
    'melon',
    'peach',
    'orange',
    'lemon',
    'blueberry'
]

def clear():
	if 	os.name == 'nt':
		os.system('cls')

	else :
		os.system('clear')


def draw(good_guess, bad_guess , secret):
	clear()

	print("Strikes : {}/7".format(len(bad_guess)))

	for letter in bad_guess:
		print(letter,end=' ')
    
	print('\n\n')

	for letter in secret:
		if letter in good_guess:
			print(letter,end=' ')

		else:
			print('_',end='')


def get_guess(good_guess, bad_guess):
	
	while True:
		print('\n\n')
		guess = input("Guess a letter").lower()

		if len(guess) != 1:
			print("Enter one letter at a time")
			continue

		elif guess in bad_guess or guess in good_guess:
			print("You have entered the letter before")
			continue

		elif not guess.isalpha():
			print("Enter a letter only")

		else:
			return guess


def play(done):
	
	secret = random.choice(fruits)

	bad_guess = []
	good_guess = []

	while True:
		draw(good_guess,bad_guess,secret)
		guess = get_guess(good_guess, bad_guess)

		if guess in secret:	
			good_guess.append(guess)
			found = True
			for letter in secret:
				if letter not in good_guess:
					found = False

			if found:
				clear()
				print("\nYou win")
				print("\n\nSecret word was : {}\n".format(secret))
				done = True

		else:
			bad_guess.append(guess)
			if len(bad_guess) > 6:
				clear()
				draw(good_guess, bad_guess, secret)
				print("\n\nYou lost. Boo Hoo!!!!")
				print("\n\nMy secret word was : {}\n\n".format(secret))
				done= True


		if done:
			play_again = input("Do you want to play again Y/n").lower()
			if play_again != 'n':
				return play(done=False)
				
			else:
				sys.exit()

def welcome():
	print("******Welcome to letter Guess Game!!!*****")
	play=input("Press Enter to Play or q to exit").lower()

	if play == 'q':
		print("Bye")
		sys.exit()

	else:
		return True

done = False



while True:
	clear()
	welcome()
	play(done)
