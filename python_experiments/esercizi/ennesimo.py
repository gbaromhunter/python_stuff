class User:
    """A class defining a user"""

    def __init__(self, first_name, last_name, age, sex, city):
        """initialise the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.sex = sex
        self.city = city

    def describe_user(self):
        """prints a summary of the user and a greeting"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()} from {self.city.title()}. You are {self.age} "
              f"years old "
              f"and "
              f"you're a "
              f"{self.sex}.")

users = []
new_user = User(input('Insert the first name: '),
                input('Insert the last name: '),
                input('Insert the age: '),
                input('Insert the sex: '),
                input('Insert the city: '))
users.append(new_user)
print(users)