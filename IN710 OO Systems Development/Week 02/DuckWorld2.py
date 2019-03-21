class FlyWithWings:
    def __call__(self, *args, **kwargs):
        print("Flying! (flap flap)")


class FlyNoWay:
    def __call__(self, *args, **kwargs):
        print("Just staying put!")


class FlyRocketPowered:
    def __call__(self, *args, **kwargs):
        print("Flying! (vroooom)")


class Duck:
    def __init__(self):
        self.fly = None

    def set_fly(self, f):
        self.fly = f

    @staticmethod
    def swim():
        print("I'm swimming!")

    def display(self):
        print("A duck of some sort...")


class MallardDuck(Duck):
    def __init__(self):
        self.fly = FlyWithWings()

    def display(self):
        super(MallardDuck, self).display()
        print("A Mallard in this case.")


class RubberDuck(Duck):
    def __init__(self):
        self.fly = FlyNoWay()

    def display(self):
        super(RubberDuck, self).display()
        print("Rubber ducky, you're the one...")


class ModelDuck(Duck):
    def __init__(self):
        self.fly = FlyNoWay()

    def display(self):
        super(ModelDuck, self).display()
        print("I'm a model duck...")


if __name__ == "__main__":

    m = MallardDuck()
    m.display()
    m.fly()
    m.swim()

    r = RubberDuck()
    r.display()
    r.fly()
    r.swim()

    md = ModelDuck()
    md.display()
    md.fly()
    md.swim()
    md.set_fly(FlyRocketPowered())
    md.fly()
