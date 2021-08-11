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
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seat(s) left".format(MAX_TICKETS - count))

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

    count += 1
    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file




