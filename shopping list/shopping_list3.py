shopping = []

def  show_help():
	print("Seperate Each item by comma")
	print("Input DONE when done, SHOW to show present list and HELP to get this message again")


def show_list():
	count = 1
	for item in shopping:
		print("{} : {}".format(count,item))
		count += 1

print("Give me some items to shop")
show_help()
while True:
	new_item = input(">")

	if new_item == "DONE":
		print("Here is Your List:")
		show_list()
		break

	elif new_item == "SHOW":
		print("Items in Cart are :")
		show_list()

	elif new_item == "HELP":
		show_help()

	else:
		new_list = new_item.split(",")

		index = input("Press Enter to put items at end of list "
			"or give me a spot to put in.There are {} items in List".format(len(shopping)))

		if index:
			spot = int(index)-1

			for item in new_list:
				shopping.insert(spot,item.strip())
				spot += 1

		else:
			for item in new_list:
				shopping.append(item.strip())
