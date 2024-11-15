class RestaurantManagementSystem:
    def __init__(self):
        # Menu with 20 dishes and their prices
        self.menu = {
            1: {"name": "Margherita Pizza", "price": 80},
            2: {"name": "Pepperoni Pizza", "price": 90},
            3: {"name": "Veggie Burger", "price": 749},
            4: {"name": "Chicken Burger", "price": 49},
            5: {"name": "Grilled Cheese Sandwich", "price": 99},
            6: {"name": "Caesar Salad", "price": 99},
            7: {"name": "Greek Salad", "price": 99},
            8: {"name": "Spaghetti Bolognese", "price": 149},
            9: {"name": "Penne Alfredo", "price": 199},
            10: {"name": "Grilled Chicken", "price": 199},
            11: {"name": "Tacos", "price": 99},
            12: {"name": "Fish and Chips", "price": 149},
            13: {"name": "Chicken Wings", "price": 49},
            14: {"name": "Beef Steak", "price": 199},
            15: {"name": "Lamb Chops", "price": 149},
            16: {"name": "Fried Rice", "price": 99},
            17: {"name": "Chicken Curry", "price": 49},
            18: {"name": "Paneer Tikka", "price":49},
            19: {"name": "Vegetable Soup", "price": 99},
            20: {"name": "Garlic Bread", "price": 99},
        }
        self.orders = []

    def display_menu(self):
        print("\n--- Menu ---")
        for id, dish in self.menu.items():
            print(f"{id}. {dish['name']} - {dish['price']:.2f}")

    def place_order(self):
        self.display_menu()
        order = []
        while True:
            try:
                dish_id = int(input("\nEnter the dish ID to order (0 to finish): "))
                if dish_id == 0:
                    break
                if dish_id in self.menu:
                    quantity = int(input(f"Enter quantity for {self.menu[dish_id]['name']}: "))
                    order.append({"dish": self.menu[dish_id], "quantity": quantity})
                else:
                    print("Invalid dish ID. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        if order:
            self.orders.append(order)
            print("\nOrder placed successfully!")
        else:
            print("No items added to the order.")

    def view_orders(self):
        if not self.orders:
            print("\nNo orders have been placed yet.")
            return
        print("\n--- Orders ---")
        for i, order in enumerate(self.orders, start=1):
            print(f"\nOrder {i}:")
            total = 0
            for item in order:
                name = item['dish']['name']
                price = item['dish']['price']
                quantity = item['quantity']
                total += price * quantity
                print(f"  {name} (x{quantity}) - ${price * quantity:.2f}")
            print(f"  Total: ${total:.2f}")

    def run(self):
        while True:
            print("\n--- Restaurant Management System ---")
            print("1. Display Menu")
            print("2. Place Order")
            print("3. View Orders")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.place_order()
            elif choice == "3":
                self.view_orders()
            elif choice == "4":
                print("Thank you for using the Restaurant Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    rms = RestaurantManagementSystem()
    rms.run()
