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


what_sacks = yes_no("Do you what sacks?")