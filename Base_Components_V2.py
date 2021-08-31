# Import Statements
import re
# Functions go here

# Checks that the name on the ticket is not blank

# Get name (can't be blank)
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This field can NOT be blank")

# integer checker


def int_check(question):
    error = "Please enter a whole number between 12 amd 130."
    valid = False
    while not valid:

        # ask the user for a number and check it is valid
        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)


def sting_check(choice, options):

    for var_list in options:

        # if the snack is in one of the list, return the full
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "Invalid Choice"

def get_snack():


    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item  in valid snacks is a list with valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "OJ", "oj", "juice", "e"],
    ]

    yes_no = [
        ["yes", "y"],
        ["no", "n"]
    ]

    # holds snack order for a single user
    snack_order = []

    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you what to order snacks? ").lower()
        check_snack = sting_check(want_snack, yes_no)

    # if they say yes
    if check_snack == "Yes":


        desired_snack = " "
        while desired_snack != "xxx":

            snack_row = []

            # ask user for desired snack and put it in lower case
            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx":
                return snack_order

            # if item has a number
            if re.match(number_regex, desired_snack):
                amount = int(desired_snack[0])
                desired_snack = desired_snack[1:]

            else:
                amount = 1
                desired_snack = desired_snack

            # check if snack is valid
            snack_choice = sting_check(desired_snack, valid_snacks)

            # check if snack amount is valid
            if amount >= 5:
                print("Sorry - we have a four snack maximum")
                snack_choice = "Invalid choice"

            # add snack AND amount to list
            snack_row.append(amount)
            snack_row.append(snack_choice)

            # check that the snack is not the exit code before adding
            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_row)


    # Show snack orders
    print()
    if len(snack_order) == 0:
        print("Snacks Ordered: None")

    else:
        print("Snacks Ordered:")

        for item in snack_order:
            print(item)


    # loop six times
    for item in range(0, 6):
        # ask user for desired snack and put it in lower case
        desired_snack = input("Snack: ").lower()

        # check if snack is valid
        snack_choice = sting_check(desired_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        print(get_snack())



# Main Routine goes here

# ********** Main Routine **********

# Main Routine goes here

# Set up dictionary's/lists to hold data

# Ask the user if they have used to program before and give instructions if necessary

# Loop to get ticket details


ticket_sales = 0
ticket_count = 0
MAX_TICKETS = 5
name = ""
profit = 0

# More lists
all_names = []
all_tickets = []

# Data Frame Dictionary
move_data_dict = {
    "Name": all_names,
    "Ticket": all_tickets
}

while name != "xxx" and ticket_count < MAX_TICKETS:
    if ticket_count < 4:
        print("You have {} seat(s) left".format(MAX_TICKETS - ticket_count))
    else:
        print("There is only 1 seat left!")

    #   Get details...

    name = not_blank("Name: ")
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")
    if age == "xxx":
        break

    if age <= 12:
        print("You are two young to watch this film!")
        continue
    elif age >= 130:
        print("You are too old to watch this film, or this input was a mistake!")
        continue

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age >= 65:
        ticket_price = 6.5
    else:
        ticket_price = 10.5

    ticket_count += 1
    ticket_sales += ticket_price

ticket_profit = (ticket_sales - ( 5 * ticket_count))
print("Ticket Profit: ${:.2f}".format(ticket_profit))


if ticket_count == MAX_TICKETS:
    print("You have sold all of the available tickets!")
else:
    print("You have sold {} tickets, There are {} places still available" .format(ticket_count, MAX_TICKETS - ticket_count))

print(get_snack())

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file



