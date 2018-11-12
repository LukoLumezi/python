print "Welcome to the Food management program"

menu = {}


while True:
    meal = raw_input("Please enter a meal: ")
    price = raw_input("Please enter the price: ")
    print "Your meal is: " + meal + "," + price

    menu[meal] = price

    new = raw_input("Would you like to enter new meal? (yes/no)")

    if new == "no":
        break


for meal in menu:
    print meal, menu[meal]
    menu_file.write("%s: %s kn\n" % (meal, menu[meal]))



todo_file.close()
print "END"