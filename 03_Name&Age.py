def int_check(question):
    error = "Please enter a whole number between 12 amd 130."

    valid = False
    while not valid:

        # ask the user for a number and check it is valid
        try:
            response = int(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seat(s) left".format(MAX_TICKETS - count))

    #   Get details...
    name = input("Name: ")
    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print("You are two young to watch this film!")
        continue
    elif age > 130:
        print("You are too old to watch this film, or this input was a mistake!")
        continue

    count += 1


    print()


    if count == MAX_TICKETS:
        print("You have sold all of the available tickets!")
    else:
        print("You have sold {} tickets.    \n"
              "There are {} places still available"
              .format(count, MAX_TICKETS - count))
