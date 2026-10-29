# 7. Movie Ticket Booking 
# Ticket price = ₹200 
# Number of tickets = 5 
# Calculate: 
# Total cost 
# GST @ 12% 
# Final amount 

ticket_price = 200
number_of_tickets = 5

total_cost = ticket_price * number_of_tickets
gst = total_cost * 0.12
final_amount = total_cost + gst

print("Total Cost: Rs.", total_cost)
print("GST @ 12%: Rs.", gst)
print("Final Amount: Rs.", final_amount)