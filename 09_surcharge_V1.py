
def sting_check(choice, options):

    for var_list in options:
        # if the snack is in one of the list, return the full
        is_valid = ""
        chosen = ""

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
        return "invalid choice"


# Main Routine

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# Loop until exit code

name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method, (cash, credit)? ").lower()
        how_pay = sting_check(how_pay, pay_method)

    # Ask for subtotal (for testing purposes)
    subtotal = float(input("Subtotal $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal ${:.2f} | Surcharge ${:.2f} | Total Payable ${:.2f}"
          .format(name, subtotal, surcharge, total))





