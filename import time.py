import time

def display_menu():
    print("\n" + "="*50)
    print("{:^50}".format("🛒 HOPKINS AND EDWARDS WHOLESALE MENU 🛒"))
    print("="*50)
    print("| {:<2} | {:<42} |".format("1", "View Product Catalog"))
    print("| {:<2} | {:<42} |".format("2", "Add Item to Cart"))
    print("| {:<2} | {:<42} |".format("3", "Remove Item from Cart"))
    print("| {:<2} | {:<42} |".format("4", "View Cart"))
    print("| {:<2} | {:<42} |".format("5", "Checkout"))
    print("| {:<2} | {:<42} |".format("6", "Exit"))
    print("="*50)


def view_catalog():
    print("="*60)
    print("{:^60}".format("📦 PRODUCT CATALOG 📦"))
    print("="*60)
    for product, details in products.items():
        stock_alert = " (Low Stock!)" if details['stock'] < 5 else ""
        print(f"{product}: ${details['price']} | Stock: {details['stock']}{stock_alert}")

def add_to_cart():
    print("\n🛒 ADD ITEM TO CART")
    print("-"*60)
    product = input("Enter product name: ").title()
    if product in products:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Invalid quantity to add!")
            elif quantity <= products[product]['stock']:
                if product in cart:
                    cart[product]['quantity'] += quantity
                else:
                    cart[product] = {'price': products[product]['price'], 'quantity': quantity}
                products[product]['stock'] -= quantity
                print(f"{quantity} {product}(s) added to cart.")
            else:
                print("Insufficient stock!")
        except ValueError:
            print("Please enter a valid number for the quantity.")
    else:
        print("Product not found!")

def remove_from_cart():
    print("\n🗑️ REMOVE ITEM FROM CART")
    print("-"*60)
    product = input("Enter product name to remove: ").title()
    if product in cart:
        try:
            quantity = int(input("Enter quantity to remove: "))
            if quantity <= 0:
                print("Invalid amount to remove!")
            elif quantity >= cart[product]['quantity']:
                products[product]['stock'] += cart[product]['quantity']
                del cart[product]
                print(f"All {product}(s) removed from cart.")
            else:
                cart[product]['quantity'] -= quantity
                products[product]['stock'] += quantity
                print(f"Removed {quantity} {product}(s) from cart.")
        except ValueError:
            print("Please enter a valid number for the quantity.")
    else:
        print("Product not in cart!")

def view_cart():
    print("\n===== SHOPPING CART =====")
    if not cart:
        print("Cart is empty.")
    else:
        total = 0
        for product, details in cart.items():
            item_total = details['price'] * details['quantity']
            print(f"{product}: {details['quantity']} x ${details['price']} = ${item_total}")
            total += item_total
        print(f"Subtotal: ${total}")

def checkout():
    print("\n===== HOPKINS AND EDWARDS WHOLESALE =====")
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return

    while True:
        subtotal = sum(details['price'] * details['quantity'] for details in cart.values())
        sales_tax = 0.1 * subtotal
        total = subtotal + sales_tax

        if total > 5000:
            discount = 0.05 * total
            total -= discount
            print(f"Discount Applied (5%): ${discount:.2f}")
        else:
            discount = 0

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (10%): ${sales_tax:.2f}")
        print(f"Total Amount Due: ${total:.2f}")

        try:
            amount_paid = float(input("Enter amount received: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if amount_paid >= total:
            change = amount_paid - total
            print(f"Change: ${change:.2f}")
            generate_receipt(subtotal, sales_tax, total, amount_paid, change)
            cart.clear()
            break
        else:
            print("Insufficient payment.")
            response = input("Would you like to remove items from the cart to reduce the total? (yes/no): ").lower()
            if response.startswith("y"):
                view_cart()
                remove_from_cart()
            else:
                print("Transaction cancelled.")
                break

def generate_receipt(subtotal, sales_tax, total, amount_paid, change):
    print("\n" + "="*40)
    print("{:^40}".format("HOPKINS AND EDWARDS WHOLESALE"))
    print("{:^40}".format("SALES RECEIPT"))
    print("="*40)
    print("{:<20}{:>5}{:>7}{:>8}".format("Item", "Qty", "Price", "Total"))
    print("-"*40)

    for product, details in cart.items():
        item_total = details['quantity'] * details['price']
        print("{:<20}{:>5} x{:>6.2f}{:>8.2f}".format(
            product, details['quantity'], details['price'], item_total))

    print("-"*40)
    print("{:<30}${:>8.2f}".format("Subtotal:", subtotal))
    print("{:<30}${:>8.2f}".format("Sales Tax (10%):", sales_tax))
    print("{:<30}${:>8.2f}".format("Total Due:", total))
    print("{:<30}${:>8.2f}".format("Amount Paid:", amount_paid))
    print("{:<30}${:>8.2f}".format("Change:", change))
    print("="*40)
    print("{:^40}".format("Thank You for Shopping with Us!"))
    print("="*40 + "\n")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            view_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid option, please try again.")

products = {
    "Apple": {"price": 70.00, "stock": 10},
    "Banana": {"price": 100.50, "stock": 15},
    "Orange": {"price": 80.75, "stock": 12},
    "Milk": {"price": 150.50, "stock": 18},
    "Bread": {"price": 200.00, "stock": 45},
    "Rice": {"price": 120.00, "stock": 20},
    "Sugar": {"price": 114.50, "stock": 18},
    "Salt": {"price": 110.50, "stock": 20},
    "Eggs": {"price": 105.00, "stock": 26},
    "Chicken": {"price": 250.00, "stock": 30},
}

cart = {}

if __name__ == "__main__":
    main()