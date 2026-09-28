# week5_lab.py
# Author: Jazmin Joseph
# Business Domain: Catering

product_name = "Sandwich Platter"
status = "Pending"
quantity = 12
unit_price = 112.50
is_over_limit = unit_price * quantity > 1000.00

print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

subtotal = quantity * unit_price
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print(subtotal, tax, total, requires_approval)

print("=== Purchase Request Summary ===")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print(f"Requires Approval: {requires_approval}")

# Step 6

user_qty = int(input("Enter a new quantity: "))
new_total = user_qty * unit_price * 1.07
print(f"New Total for {user_qty} units: ${new_total:.2f}")
print(f"Requires Approval: {new_total > 1000}")
