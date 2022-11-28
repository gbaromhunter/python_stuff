
# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.

class Restaurant:
    """An object depicting a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialise attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    # Make a method called describe_restaurant() that prints these two pieces of
    # information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The restaurant's name is {self.restaurant_name} and it's cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """print open to business message"""
        print(f"The {self.restaurant_name} is now open to business!")

    def check_served(self):
        """check how many customers had been served"""
        print(f"The restaurant has served {self.number_served} clients.")

    def set_number_served(self, served):
        """set the number of served people to a certain number"""
        self.number_served = served
        print(f"You have set the customer served to {served} for {self.restaurant_name}")

    def increment_number_served(self, increment):
        """increment the served number by a value"""
        self.number_served += increment
        print(f"You have added {increment} clients to the served ones.")

class IceCreamStand(Restaurant):
    '''Describe an ice cream stand'''
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def store_flavours(self, flavour):
        self.flavours.append(flavour)
        print(f"You have added this flavour: {flavour}")

    def check_flavours(self):
        print(f"The ice cream stand offers the following flavours: {self.flavours}")

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you like that could represent how many
# customers were served in, say, a
# day of business