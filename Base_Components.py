# Import Statements

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

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file




