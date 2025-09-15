# Take input from user
total_price = float(input("Enter the total price of grocery items: "))

# Apply discount
if total_price > 1500:
    discount = total_price * 0.10
    discount_percentage = 10
else:
    discount = total_price * 0.05
    discount_percentage = 5

# Calculate the amount to be paid
amount_to_be_paid = total_price - discount

# Print the result
print(f"Total Price: {total_price}")
print(f"Discount ({discount_percentage}%): {discount}")
print(f"Amount to be Paid: {amount_to_be_paid}")
