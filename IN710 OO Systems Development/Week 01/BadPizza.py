class Pizza():
    def __init__(self, name, baseCost, toppings):
        self.toppings = toppings
        self.name = name
        self.baseCost = baseCost

    def get_name(self):
        topping_names = []
        for t in self.toppings:
            if t == "olives":
                topping_names.append("Olives")
            elif t == "extra_cheese":
                topping_names.append("Extra Cheese")
            elif t == "mushrooms":
                topping_names.append("Mushrooms")
            elif t == "onions":
                topping_names.append("Onions")

        return self.name + (" with " + " and ".join(topping_names)) if topping_names else ""

    def get_cost(self):
        toppingsCost = 0
        for t in self.toppings:
            if t == "olives":
                toppingsCost += 2
            elif t == "extra_cheese":
                toppingsCost += 1
            elif t == "mushrooms":
                toppingsCost += 2
            elif t == "onions":
                toppingsCost += 1
        return self.baseCost + toppingsCost


if __name__ == "__main__":
    p = Pizza("Hawaii", 20, ['extra_cheese', 'olives'])
    print("%s: $%.2f" % (p.get_name(), p.get_cost()))
