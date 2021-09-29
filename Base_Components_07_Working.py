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

# !!!! Missing function check tickets !!!!
def check_tickets(tickets_sold, ticket_limit):

    if tickets_sold < ticket_limit - 1:
        print("You have {} places left".format(ticket_limit - tickets_sold))
    #  on place left
    else:
        print("*** There is ONE seat left! ***")

    return ""

# get ticket price
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

# String check
def string_check(choice, options):

    for var_list in options:
        is_valid = ""
        chosen = ""

        # if the snack is in one of the list, return the full
        if choice in var_list:
            # Get full name of snack and put it in title case so it looks nice when outputted
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

# Get snacks
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

# Format currency
def currency (x):
    return "${:.2f}".format(x)


# ********** Main Routine **********
# Initalise variables
MAX_TICKETS = 5
ticket_sales = 0
ticket_count = 0
name = ""

# Empty lists to store orders
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

surcharge_multi_list = []

summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit","Total Profit"]

summary_data = []

pay_method = [
    ["cash", "ca"],["credit", "cr"]
]

yes_no = [
    ["yes", "y"],["no", "n"]
]


# *** Dictionaries ****

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

# Summary Dictionary
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

# Data Frame Dictionary for everything that is a price
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}


# Ask the user if they have used to program before and give instructions if necessary
print(" *** INSTRUCTIONS *** \n"
      "\n"
        "1. When the program asks you to, input your name press the <enter> key. \n"
        "2. When the program asks you to, input your age press the <enter> key. \n"
        "3. Then if you want snacks (if you do not  want snacks skip to step 4), \n"
        "   (to see what snacks are available look at 'more details'  \n"
        "   enter want snack you want and press the <enter> key. \n"
        "   If you want more than one snack repeat step 3. \n"
        "   Once you have all the snacks you want press the <x> three times. \n"
        "4. (if you did do step 3 skip to step 5) Press the <x> three times. \n"
        "5. Then enter your preferred payment type \n"
        "   (to see what payment types are available look at 'more details' \n"
        "6. Repeat steps one through five, for all of the other people that are watching the movie with you. \n"
        "   When you have done step six press the 'x' key three times \n"
        "7. If you done step six correctly you should see a order summary \n"
        "8. Press the 'x' three times to end the program \n")

print(" *** MORE DETAILS *** \n"
      "\n"
    "Avaibale Snacks: \n"
      "\n"
        "Popcorn:           Price: $2.50 \n"
        "Water:             Price: $2.00 \n"
        "Pita Chips:        Price: $4.50 \n"
        "M&Ms:              Price: $3.00 \n"
        "Orange Juice:      Price: $3.25 \n"
      "\n"
      "\n"
      "Available Payment Types:\n"
      "\n"
      "Credit (5% surcharge)\n"
      "Cash \n"
      )

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:
    # !!!! check number of tickets in function !!!
    check_tickets(ticket_count, MAX_TICKETS)

    # !!! Get ticket details !!!
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
    snack_order = get_snack()

    # assume snacks purchased
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

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
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")

#Create snacks dataframe
movie_frame["Snacks"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = movie_frame["Ticket"] + movie_frame["Snacks"]

movie_frame["Surcharge"] = movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ", "Pita Chips": "Chips"})

# populate snack items
for item in snack_lists:
    # add to summary data
    summary_data.append(sum(item))

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

# !!!! set columns to be printed!!!!
pandas.set_option('display.max_columns', None)
# display to 2 dp
pandas.set_option('precision', 2)

# !!!! Output !!!
print()
print(" *** Ticket / Snack Information *** ")
print("Note: for full details, please refer to the exel document")
print()
print(movie_frame[["Ticket", "Snacks", "Sub Total","Surcharge", "Total"]])
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

