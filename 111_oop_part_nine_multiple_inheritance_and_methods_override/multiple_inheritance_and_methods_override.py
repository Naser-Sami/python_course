# ------------------------------------------------
# -- Object Oriented Programming => Inheritance --
# ------------------------------------------------

class Food:  # Base Class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} Is Created From Base Class.\nPrice is {self.price}")

    def eat(self):
        print("Eat Method From Base Class")


class Apple(Food):  # Derived Class
    def __init__(self, name, price, amount):
        # Food.__init__(self, name, price)   # Create Instance From Base Class
        super().__init__(name, price)
        self.amount = amount

        print(f"{self.name} Is Created From Derived Class.\nPrice is {self.price}, and amount {self.amount}")

    def print_message(self):
        print("Hello World!")

    # Override Method
    def eat(self):
        print("Eat Override Method From Derived Class")


# food_one = Food("Pizza", 13)
food_two = Apple("Pizza", 20, 2)
# food_two.eat()
