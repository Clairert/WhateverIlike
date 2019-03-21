from abc import ABC, abstractmethod

class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("Flying! (flap flap)")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("Just staying put!")

class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("Flying! (vroooom)")

class Duck(object):
    def __init__(self):
        self.fly_behaviour = FlyBehaviour()

    def set_fly_behaviour(self, fb):
        self.fly_behaviour = fb

    def swim(self):
        print("I'm swimming!")

    def display(self):
        print("A duck of some sort...")

    def perform_fly(self):
        self.fly_behaviour.fly()

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyWithWings()

    def display(self):
        super(MallardDuck, self).display()
        print("A Mallard in this case.")

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyNoWay()

    def display(self):
        super(RubberDuck, self).display()
        print("Rubber ducky, you're the one...")

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyNoWay()

    def display(self):
        print("I'm a model duck...")

if __name__ == "__main__":

    m = MallardDuck()
    m.display()
    m.perform_fly()
    m.swim()

    r = RubberDuck()
    r.display()
    r.perform_fly()
    r.swim()

    md = ModelDuck()
    md.display()
    md.perform_fly()
    md.swim()
    md.set_fly_behaviour(FlyRocketPowered())
    md.perform_fly()
