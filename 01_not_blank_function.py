# function goes here

def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This field can NOT be blank please enter your name")


name = not_blank("Name: ")
