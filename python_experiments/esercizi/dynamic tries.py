
class Item:

    def __init__(self, name, weight, value):
        self._name = name
        self._weight = weight
        self._value = value

    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight

    def get_value(self):
        return self._value

    def get_ratio(self):
        return self._value / self._weight

    def describe_formal(self):
        return print(f"This item is a {self._name} that weights {self._weight} and has a value of {self._value}."
                     f"It's ratio is {self.get_ratio()}")

    def describe(self):
        return print(f"{self.get_name()}: weight = {self.get_weight()}, value = {self.get_value()}, ratio = {self.get_ratio()}")


class Space:
    def __init__(self, name):
        self._name = name
        self._items = {}

    def get_name(self):
        return self._name

    def add_item(self, item):
        self._items[item.get_name()] = item

    def transfer_item(self, item_name, destination=None):
        if destination is None:
            del self._items[item_name]
        else:
            destination.add_item(self._items.pop(item_name))


    def describe(self):
        print(f"Here is the list of items in the space named: {self.get_name()}")
        for item in self._items:
            self._items[item].describe()


class Knapsack(Space):

    def __init__(self, name, weight_limit):
        super().__init__(name)
        self.weight_limit = weight_limit

    def get_weightlimit(self):
        return self.weight_limit

    def add_item(self, item):
        if sum([item.get_weight for item in self._items.values()]) >= self.get_weightlimit():
            raise ValueError(f"You are carrying too much!")
        else:
            self._items[item.get_name()] = item

    def transfer_item(self, item_name, destination=None):
        if destination is None:
            del self._items[item_name]
        else:
            try:
                destination.add_item(self._items.pop(item_name))
            except:
                return print("You are carrying too much to transfer this item")



def create_test_space():
    space = Space("House")
    space.add_item(Item("Computer", 3, 200))
    space.add_item(Item("Clock cuckoo", 10, 100))
    space.add_item(Item("Lamp", 5, 50))
    space.add_item(Item("Chair", 12, 40))
    space.add_item(Item("Gold ring", 1, 200))
    space.add_item(Item("Amber pendant", 1, 150))
    space.add_item(Item("Plasma TV", 16, 1200))
    space.add_item(Item("Silver cup", 2, 100))
    space.add_item(Item("Bronze antique shield", 6, 1500))
    knapsack = Knapsack("Knapsack", 40)
    return space, knapsack

def run_test_describe():
    global house, knapsack
    house, knapsack = create_test_space()
    house.describe()
    knapsack.describe()
def run_test_addknap():
    for item in house._items.values():
        house.transfer_item(item.get_name(), knapsack)