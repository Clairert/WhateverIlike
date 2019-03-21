from BetterPizza import BetterPizza, Topping

class Order():
    items = []

    def add(self, item):
        self.items.append(item)

    def print_order(self):
        for i in self.items:
            print("%s: $%.2f" % (i.get_name(), i.get_cost()))
        
if __name__ == "__main__":
    o = Order()
    o.add(BetterPizza("Hawaii", 20, [Topping("Extra Cheese", 1), Topping("Olives", 2)]))
    o.add(BetterPizza("Salami", 20, [Topping("Extra Cheese", 1), Topping("Chilli", 1.5)]))
    o.print_order()
