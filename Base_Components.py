# Import Statements

# Functions go here
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("This field can NOT be blank,"
                  "please enter you name.")
# Checks that the name on the ticket is not blank

# ********** Main Routine **********

# Main Routine goes here

# Set up dictionary's/lists to hold data

# Ask the user if they have used to program before and give instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file




