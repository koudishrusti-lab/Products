import sys

print("=== Product Details Program ===")

if len(sys.argv) == 4:
    # Values from Jenkins command
    product_name = sys.argv[1]
    product_id = sys.argv[2]
    product_price = sys.argv[3]
else:
    # Fallback to manual input (for local testing)
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    product_price = input("Enter Product Price: ")

print("\nProduct Details:")
print("ID:", product_id)
print("Name:", product_name)
print("Price:", product_price)
