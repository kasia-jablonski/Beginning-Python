TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100  

def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:

    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("How many tickets would you like, {}?  ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {} Please try again".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed?   Y/N   ")

        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you, {}".format(name))

print("Sorry the tickets are all sold out!")
