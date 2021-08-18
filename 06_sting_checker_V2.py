
# valid snacks holds list of all snacks
# Each item  in valid snacks is a list with valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "OJ", "oj", "juice", "e"]

]

# variables
snack_ok = ""
snack = ""

# loop 3 times for testing
for item in range(0, 3):

    # ask user desired snack and put it in lower case
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        if desired_snack in var_list:

            # Get full name of snack and put it in
            # title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "Yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "No"

    # if the snack is not OK - ask question again
    if snack_ok == "Yes":
        print("Snack Choice: ", snack)
    else:
        print("Invalid Choice")









