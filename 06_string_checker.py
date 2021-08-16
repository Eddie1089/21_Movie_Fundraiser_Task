

# string checking functions, takes in
# question and list of valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
            # checks if the response is the first letter of an item in the list(to_check)

                if response in item[0]:
                    # note returns the whole response
                    return item

        print("That is not a valid response")


want_snacks = string_checker("Do you want snacks?", ["yes","no"])

