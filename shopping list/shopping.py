shopping = []

print("Enter Your shopping List")
print("Enter DONE to exit")

while 1:
    new_item = input(">")

    if new_item == 'DONE':
        show()
        break

    shopping.append(new_item)
def show:
    for item in shopping:
        print(item)
