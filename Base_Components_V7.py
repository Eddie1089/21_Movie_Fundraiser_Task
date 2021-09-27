# Import Statements
import re
import pandas
# Functions go here

# Get name (can't be blank)


def not_blank(question):
    valid = False
    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This field can NOT be blank")


def currency (x):
    return "${:.2f}".format(x)

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


def string_check(choice, options):

    for var_list in options:
        is_valid = ""
        chosen = ""

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
        print("Please enter a valid option")
        return "invalid choice"


def get_ticket_price():
    # Get age (between 12 and 130)
    age = int_check("Age: ")

    if age <= 12:
        print("You are too young to watch this film!")
        return "invalid ticket price"
    elif age >= 130:
        print("You are too old to watch this film, or this input was a mistake!")
        return "invalid ticket price"

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age <= 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


def get_snack():
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    valid_snacks = [
        ["popcorn", "p", "corn", "pop", "a"],
        ["M&Ms", "m&ms", "mms", "m", "mm", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h20" , "d"],
        ["orange juice", "OJ", "oj", "juice", "e"],
    ]
    # holds snack order for a single user
    snack_order = []
    desired_snack = ""

    while desired_snack != "xxx" or desired_snack != "n":
        snack_row = []

        # ask user for desired snack and put it in lower case
        desired_snack = input("Snack: ").lower()
        if desired_snack == "xxx" or desired_snack == "n":
            return snack_order

        # if number in input
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >=5:
            print("Sorry there is a 5 snack max")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)


# ********** Main Routine **********
# Lists and Variables
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

ticket_sales = 0
ticket_count = 0
MAX_TICKETS = 5
name = ""
profit = 0

# More lists
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []


surcharge_multi_list = []
get_order = []


summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]


summary_data = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]



# Data Frame Dictionary for everything that is not a price
movie_data_dict = {
    "Name": all_names,
    "Ticket": all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice,
    "Surcharge_Multiplier": surcharge_multi_list
}

# Data Frame Dictionary for everything that is a price
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}

summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

print("Do you what the code tells you to do")


# Ask the user if they have used to program before and give instructions if necessary

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:
    if ticket_count < 4:
        print("You have {} seat(s) left".format(MAX_TICKETS - ticket_count))
    else:
        print("There is only 1 seat left!")

    #   Get details...
    name = not_blank("Name: ")
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # If age is invalid restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # Add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you what to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)
    if check_snack == "Yes":
        snack_order = get_snack()
    else:
        snack_order = []

    print()
    if len(snack_order) == 0:
        print("Snacks ordered: None")
    else:
        print("Snacks Ordered: ")
        print(snack_order)

    # Assume that no snacks have been brought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Payment method

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method(cash, credit)? ").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0
    surcharge_multi_list.append(surcharge_multiplier)


# Print details...
print()
print("Popcorn: ", snack_lists[0])
print("M&Ms: ", snack_lists[1])
print("Pita Chips: ", snack_lists[2])
print("Water: ", snack_lists[3])
print("Orange Juice: ", snack_lists[4])
print()


movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")

# Create column called "Sub Total"
# Fill it with price for snacks and ticket

movie_frame["Snacks"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Snacks"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips"})


# Set up summary dataframes and populating snacks
snack_total = movie_frame["Snacks"].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get ticket profit and add it to lists
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# Work out total profit and add it to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Create summary frame (not working)
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index("Item")

# **** Pre printing / Export ****
# format currency values
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# witre each to a different file
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")




# **** Printing ****
print()
print(" *** Ticket / Snack Information *** ")
print("Note: for full details, please refer to the exel document")
print()
print(movie_frame[["Ticket", "Snacks", "Sub Total",
                   "Surcharge", "Total"]])

print(movie_frame)


print()
print( "*** Snack & Profit Summary ***")
print(summary_frame)

# Get ticket profit
ticket_profit = (ticket_sales - (5 * ticket_count))
print("Ticket Profit: ${:.2f}".format(ticket_profit))

# Tell the user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all of the available tickets!")
else:
    print("You have sold {} tickets, There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))

print(get_snack())

# Output to CSV file
