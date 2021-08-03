# Import Statements

# Functions go here

# Checks that the name on the ticket is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response

        # if  name is blank show error, and repeat loop
        else:
            print(error_message)


# Main Routine goes here
name = not_blank("Name: ",
                 "This field can NOT be blank, "
                 "please enter your name")
# ********** Main Routine **********

# Main Routine goes here

# Set up dictionary's/lists to hold data

# Ask the user if they have used to program before and give instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary (5%))

# Calculate sales and profit

# Output to CSV file




