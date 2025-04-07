import time

def display_menu():
    print("\n===== POS SYSTEM MENU =====")
    print("1. View Product Catalog")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

def view_catalog():
    print("\n===== PRODUCT CATALOG =====")
    for product, details in products.items():
        stock_alert = " (Low Stock!)" if details['stock'] < 5 else ""
        print(f"{product}: ${details['price']} | Stock: {details['stock']}{stock_alert}")

def add_to_cart():
    product = input("Enter product name: ").title()
    if product in products:
        quantity = int(input("Enter quantity: "))
        if quantity <= products[product]['stock']:
            if product in cart:
                cart[product]['quantity'] += quantity
            else:
                cart[product] = {'price': products[product]['price'], 'quantity': quantity}
            products[product]['stock'] -= quantity
            print(f"{quantity} {product}(s) added to cart.")
        else:
            print("Insufficient stock!")
    else:
        print("Product not found!")

def remove_from_cart():
    product = input("Enter product name to remove: ").title()
    if product in cart:
        quantity = int(input("Enter quantity to remove: "))
        if quantity >= cart[product]['quantity']:
            products[product]['stock'] += cart[product]['quantity']
            del cart[product]
        else:
            cart[product]['quantity'] -= quantity
            products[product]['stock'] += quantity
        print(f"Removed {quantity} {product}(s) from cart.")
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
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return
    
    subtotal = sum(details['price'] * details['quantity'] for details in cart.values())
    sales_tax = 0.1 * subtotal
    total = subtotal + sales_tax
    
    if total > 5000:
        discount = 0.05 * total
        total -= discount
        print(f"Discount Applied: ${discount}")
    
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (10%): ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")
    
    while True:
        amount_paid = float(input("Enter amount received: "))
        if amount_paid >= total:
            change = amount_paid - total
            print(f"Change: ${change:.2f}")
            generate_receipt(subtotal, sales_tax, total, amount_paid, change)
            cart.clear()
            break
        else:
            print("Insufficient payment. Please enter a valid amount.")

def generate_receipt(subtotal, sales_tax, total, amount_paid, change):
    print("\n===== RECEIPT =====")
    print("ABC STORE")
    print("----------------------------")
    for product, details in cart.items():
        print(f"{product}: {details['quantity']} x ${details['price']} = ${details['price'] * details['quantity']}")
    print("----------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (10%): ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Change: ${change:.2f}")
    print("Thank You for Shopping with Us!")

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
    "Apple": {"price": 1.00, "stock": 10},
    "Banana": {"price": 0.50, "stock": 15},
    "Orange": {"price": 0.75, "stock": 12},
    "Milk": {"price": 3.50, "stock": 8},
    "Bread": {"price": 2.00, "stock": 5},
    "Rice": {"price": 10.00, "stock": 20},
    "Sugar": {"price": 4.50, "stock": 18},
    "Salt": {"price": 1.50, "stock": 10},
    "Eggs": {"price": 5.00, "stock": 6},
    "Chicken": {"price": 12.00, "stock": 4},
}

cart = {}

if __name__ == "__main__":
    main()
