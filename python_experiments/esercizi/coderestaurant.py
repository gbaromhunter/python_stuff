from esercizio import *

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurant1 = Restaurant('Kyoto Sushi', 'Sushi')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Burrito King', 'Mexican')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Gostilnica Purlenkite', 'Bulgarian')
restaurant3.describe_restaurant()

restaurant3.check_served()
restaurant3.set_number_served(int(input("How many people has the restaurant served?: ")))

restaurant3.check_served()
restaurant3.increment_number_served(int(input("How many customers to add? :")))
restaurant3.check_served()