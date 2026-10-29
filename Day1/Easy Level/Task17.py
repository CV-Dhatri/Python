# Task 17 
# Process order IDs and stop if a cancelled order is found. 

order_ids = ["ORD001", "ORD002", "ORD003", "ORD004", "ORD005"]
canceled_order = "ORD003"

for order_id in order_ids:
    if order_id == canceled_order:
        print(f"Cancelled order found: {order_id}. Stopping processing.")
        break
    print(f"Processing order: {order_id}")