class Car():
    def __init__(self, colour, year):
        self.colour = colour
        self.year = year

    def get_colour(self):
        return self.colour

    def get_year(self):
        return self.year

    def get_desc(self):
        return self.get_colour() + ", " + str(self.get_year())

class CarsReport():
    def generate_report(self, cars, recipient):
        filtered_cars = []
        for car in cars:
            if (self.filter_condition(car)):
                filtered_cars.append(car)

        email_subject = self.subject()
        if filtered_cars:
            email_body = "I found these cars: "
            email_body += self.format_cars(filtered_cars)
        else:
            email_body = "No new cars found."

        print(email_subject)
        print(email_body)

    def format_cars(self, filtered_cars):
        return "; ".join([c.get_desc() for c in filtered_cars])

    def filter_condition(self, car):
        raise NotImplemented()

    def subject(self):
        raise NotImplemented()


class NewCarsReport(CarsReport):
    def filter_condition(self, car):
        return car.get_year() >= 2017

    def subject(self):
        return "New Cars report"


class RedCarsReport(CarsReport):
    def filter_condition(self, car):
        return car.get_colour() == "red"

    def subject(self):
        return "Red Cars report"


class FancyRedCarsReport(RedCarsReport):
    def format_cars(self, filtered_cars):
        return "; ".join([str(c.get_year()) for c in filtered_cars])

if __name__ == "__main__":
    cars = [Car("green", 2017), Car("red", 2010), Car("white", 2018)]
    NewCarsReport().generate_report(cars, "my@email.com")
    RedCarsReport().generate_report(cars, "my@email.com")
    FancyRedCarsReport().generate_report(cars, "my@email.com")

