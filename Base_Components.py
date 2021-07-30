# Import Statements
print ()
# Functions go here

# ********** Main Routine **********
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# Main Routine goes here
name = not_blank("Name: ",
                 "This field can NOT be blank, "
                 "please enter your name")



name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seat(s) "
          "left".format(MAX_TICKETS - count))

    #   Get details...
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all of the available tickets!")
else:
    print("You have sold {} tickets.    \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))


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




