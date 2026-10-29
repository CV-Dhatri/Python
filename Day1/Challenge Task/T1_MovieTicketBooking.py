# *Challenge Task*  
# Design a Movie Ticket Booking function: 
# def book_ticket(customer_name, movie_name, tickets=1, *snacks, **details): 
# Requirements: 
# Print customer name, movie name, and number of tickets. 
# Print all snacks ordered. 
# Print theatre, seat type, payment mode, and show time. 
# Calculate the total ticket cost.

def book_ticket(customer_name, movie_name, tickets=1, *snacks, **details):
    print(f"Customer Name: {customer_name}")
    print(f"Movie Name: {movie_name}")
    print(f"Number of Tickets: {tickets}")

    if snacks:
        print("Snacks Ordered:")
        for snack in snacks:
            print(f"- {snack}")
    else:
        print("No snacks ordered.")

    theatre = details.get('theatre', 'Not specified')
    seat_type = details.get('seat_type', 'Not specified')
    payment_mode = details.get('payment_mode', 'Not specified')
    show_time = details.get('show_time', 'Not specified')

    print(f"Theatre: {theatre}")
    print(f"Seat Type: {seat_type}")
    print(f"Payment Mode: {payment_mode}")
    print(f"Show Time: {show_time}")

    ticket_price = 10 
    total_cost = tickets * ticket_price
    print(f"Total Ticket Cost: Rs.{total_cost}")


# Example usage:
book_ticket("Dhatri", "Spiderman: Brand New Day", 2, "Popcorn", "Soda", theatre="PVR", seat_type="Gold", payment_mode="Credit Card", show_time="7:00 PM")
