import re

# Function goes here


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
        # ask user for desired snack and put it in lower case
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

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
        amount_snack = "{} {}".format(amount, snack_choice)

        # check that the snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

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
