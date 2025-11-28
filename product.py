import sys

def get_product_details(prod_id, name, quantity, price):
    """Return formatted product details string"""
    return f"Product ID: {prod_id}, Name: {name}, Quantity: {quantity}, Price: {price}"

if __name__ == "__main__":
    print("=== Product Details Program ===")
    try:
        # Case 1: arguments passed (for CLI / Jenkins)
        if len(sys.argv) == 5:
            product_id = sys.argv[1]
            product_name = sys.argv[2]
            quantity = sys.argv[3]
            price = sys.argv[4]
        else:
            # Case 2: user console input
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")

        print("\n=== Entered Product Information ===")
        print("Product ID:", product_id)
        print("Product Name:", product_name)
        print("Quantity:", quantity)
        print("Price:", price)

        formatted_details = get_product_details(product_id, product_name, quantity, price)
        print("\nFormatted Output:")
        print(formatted_details)

    except ValueError:
        print("Invalid input!")
