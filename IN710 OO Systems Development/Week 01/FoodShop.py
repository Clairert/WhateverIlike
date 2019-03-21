class FoodItem(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost

class Topping(FoodItem):
    pass

# this will be read from the database
toppings_list = {
    "cheese": Topping("Extra Cheese", 1),
    "olives": Topping("Olives", 2),
    "chilli": Topping("Chilli", 1.5)
}

class Pizza(FoodItem):
    def __init__(self, name, baseCost, toppings):
        super(Pizza, self).__init__(name, baseCost)
        self.toppings = []
        for t in toppings:
            self.toppings.append(toppings_list[t])

    def get_name(self):
        topping_names = [t.get_name() for t in self.toppings]
        return self.name + (" with " + " and ".join(topping_names)) if topping_names else ""
    
    def get_cost(self):
        toppingsCost = 0
        for t in self.toppings:
            toppingsCost += t.cost
        return self.cost + toppingsCost

class Drink(FoodItem):
    def __init__(self, name, baseCost, size):
        super(Drink, self).__init__(name, baseCost)
        self.size = size

    def get_name(self):
        return super(Drink, self).get_name() + ", " + self.size
    
class Order():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def print_order(self):
        for i in self.items:
            print("%s: $%.2f" % (i.get_name(), i.get_cost()))

if __name__ == "__main__":
    o = Order()

    o.add(Pizza("Hawaii", 20, ["cheese", "olives"]))
    o.add(Pizza("Salami", 20, ["cheese", "chilli"]))
    o.add(Drink("Coke", 4, "Large"))
    o.print_order()
