def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# Main Routine goes here
name = not_blank("Name: ",
                 "This field can NOT be blank, "
                 "please enter your name")

def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} " \
            "and {}".format(low_num, high_num)

    vaild = False
    while not vaild:

            # ask the user for a number and check it is valid
            try:
                response = int(input(question))

                if low_num <= response <= high_num:
                    return response
                else:
                    print(error)

            # if an integer is not entered, display an error
            except ValueError:
                print(error)

age = int_check("Age: ", 12, 130)


