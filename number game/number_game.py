import random

secret = random.randint(1,10)


def game():
	guesses = []
	while len(guesses) <5:
			guess = int(input("Guess any number between 1 and 10:"))	
			if guess == secret:
				print("That's The Number nigga")
				break

			elif guess > secret:
				print("{} is way to higher than my number".format(guess))

			else:
				print("{} is lower than my number".format(guess))

			guesses.append(guess)

	else:
		print("You din't get It my number was {}".format(secret))

		choice = input("Do You want to play game again. Y/n")

		if choice.lower() != 'n':
			game()

		else:
			print("Bye!!")

game()
