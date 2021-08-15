def yes_no(question):

    error = "Please answer yes / no"

    valid = False
    while not valid:

        # ask question an put response in lower case
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print(error)

# Main routine goes here


for item in range(0, 6):
    want_snacks = yes_no("Do you want any snacks")
