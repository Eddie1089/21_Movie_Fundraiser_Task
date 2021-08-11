# Import Statements

# Functions go here

# Checks that the name on the ticket is not blank

# Get name (can't be blank)

# Main Routine goes here

# ********** Main Routine **********

# Main Routine goes here

# Set up dictionary's/lists to hold data

# Ask the user if they have used to program before and give instructions if necessary

# Loop to get ticket details
def int_check(question):
    error = "Please enter a whole number between 12 amd 130."

    valid = False
    while not valid:

        # ask the user for a number and check it is valid
        try:
            response = int(input(question))

            if response <=0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


name = ""
ticket_count = 0
MAX_TICKETS = 5
profit = 0

while name != "xxx" and ticket_count < MAX_TICKETS:
    print("You have {} seat(s) left".format(MAX_TICKETS - ticket_count))

    #   Get details...
    name = input("Name: ")
    if name == "xxx":
        break

    age = int_check("Age: ")

    if age < 12:
        print("You are two young to watch this film!")
        continue
    elif age > 130:
        print("You are too old to watch this film, or this input was a mistake!")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age >= 65:
        ticket_price = 6.5
    else:
        ticket_price = 10.5

        profit_made = ticket_price - 5
        profit += profit_made

        print("{} : ${:.2f}".format(name, ticket_price))

    ticket_count += 1

print("Profit from tickets: ${:.2f}".format(profit))

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file




