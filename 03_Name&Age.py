def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    valid = False
    while not valid:

            # ask the user for a number and check it is valid

            try:
                response = int(input(question))

                if low_num < response < high_num:
                    return response
                else:
                    print(error)

            # if an integer is not entered, display an error
            except ValueError:
                print(error)


name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seat(s) "
          "left".format(MAX_TICKETS - count))

    #   Get details...
    name = input("Name: ")

    if name == "xxx":
        break
    age = int_check("Age: ", 11, 131)
    count += 1
    print()

    if count == MAX_TICKETS:
        print("You have sold all of the available tickets!")
    else:
        print("You have sold {} tickets.    \n"
              "There are {} places still available"
              .format(count, MAX_TICKETS - count))
