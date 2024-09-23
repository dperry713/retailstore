class RetailStore:
    def __init__(self):
        self.inventory = {
            "Eggs": {"quantity": 50, "price": 2.99},
            "Roller Skates": {"quantity": 10, "price": 49.99},
            "Pencils": {"quantity": 100, "price": 0.99},
            "Shoes": {"quantity": 20, "price": 39.99},
            "Men's Shirts": {"quantity": 15, "price": 19.99},
            "Dog Food": {"quantity": 25, "price": 24.99},
            "Hair Dye": {"quantity": 30, "price": 9.99}
        }

    def add_product(self, product_name, quantity, price):
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] += quantity
        else:
            self.inventory[product_name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {product_name} at ${price:.2f} each.")

    def update_inventory(self, product_name, quantity):
        if product_name in self.inventory:
            self.inventory[product_name]['quantity'] = quantity
            print(f"Updated {product_name} quantity to {quantity}.")
        else:
            print(f"Product {product_name} not found in inventory.")

    def remove_product(self, product_name):
        if product_name in self.inventory:
            del self.inventory[product_name]
            print(f"Removed {product_name} from inventory.")
        else:
            print(f"Product {product_name} not found in inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for product_name, details in self.inventory.items():
                print(f"{product_name}: {details['quantity']} units at ${details['price']:.2f} each")


def main():
    store = RetailStore()

    while True:
        print("\n1. Add Product")
        print("\n2. Update Inventory")
        print("\n3. Remove Product")
        print("\n4. Display Inventory")
        print("\n5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            store.add_product(product_name, quantity, price)
        elif choice == '2':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            store.update_inventory(product_name, quantity)
        elif choice == '3':
            product_name = input("Enter product name to remove: ")
            store.remove_product(product_name)
        elif choice == '4':
            store.display_inventory()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
