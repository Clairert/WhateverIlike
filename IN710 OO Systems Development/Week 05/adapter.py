import datetime

from template_method import NewCarsReport, RedCarsReport, FancyRedCarsReport, Car


class DifferentCar():
    def __init__(self, color, manufacture_date):
        self.color = color
        self.manufacture_date = manufacture_date

    def get_manufacture_date(self):
        return self.manufacture_date

    def get_color(self):
        return self.color


class DifferentCarAdapter(Car):
    def __init__(self, differentCar):
        self._wrapped_car = differentCar

    def get_colour(self):
        return self._wrapped_car.get_color()

    def get_year(self):
        return self._wrapped_car.get_manufacture_date().year


class SimpleDifferentCarAdapter(Car):
    def __init__(self, differentCar):
        super().__init__(differentCar.get_color(), differentCar.get_manufacture_date().year)


cars = [DifferentCar("green", datetime.date(2017, 10, 10)), DifferentCar("red", datetime.date(2017, 10, 10)), DifferentCar("white", datetime.date(2017, 10, 10))]
#cars = [DifferentCarAdapter(car) for car in cars]
cars = [SimpleDifferentCarAdapter(car) for car in cars]

NewCarsReport().generate_report(cars, "my@email.com")
RedCarsReport().generate_report(cars, "my@email.com")
FancyRedCarsReport().generate_report(cars, "my@email.com")

