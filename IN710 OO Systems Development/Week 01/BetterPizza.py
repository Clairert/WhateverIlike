class Topping():
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class BetterPizza():
    def __init__(self, name, baseCost, toppings):
        self.toppings = toppings
        self.name = name
        self.baseCost = baseCost

    def get_name(self):
        topping_names = [t.name for t in self.toppings]
        return self.name + (" with " + " and ".join(topping_names)) if topping_names else ""
    
    def get_cost(self):
        toppingsCost = 0
        for t in self.toppings:
            toppingsCost += t.cost
        return self.baseCost + toppingsCost


if __name__ == "__main__":
    p = BetterPizza("Hawaii", 20, [Topping("Extra Cheese", 1), Topping("Olives", 2)])
    print("%s: $%.2f" % (p.get_name(), p.get_cost()))

    p = BetterPizza("Salami", 20, [Topping("Extra Cheese", 1), Topping("Chilli", 1.5)])
    print("%s: $%.2f" % (p.get_name(), p.get_cost()))
