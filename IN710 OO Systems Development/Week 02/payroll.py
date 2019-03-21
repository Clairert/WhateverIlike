class PaycheckCalculationStrategy():
    def paycheckAmount(self):
        raise NotImplementedError()

    def details(self):
        raise NotImplementedError()


class SalaryStrategy(PaycheckCalculationStrategy):
    def __init__(self, annualSalary):
        self.annualSalary = annualSalary

    def paycheckAmount(self):
        return (self.annualSalary / 52) *0.8

    def details(self):
        return "Paycheck calculated from $%d per year." % self.annualSalary


class HourlyRateStrategy(PaycheckCalculationStrategy):
    def __init__(self, hourlyRate):
        self.hourlyRate = hourlyRate

    def paycheckAmount(self):
        return (self.hourlyRate * 5 * 8) *0.8

    def details(self):
        return "Paycheck calculated from $%d per hour." % self.hourlyRate

class Employee:
    def __init__(self, name, remunerationStrategy):
        self.name = name
        self.remunerationStrategy = remunerationStrategy

    def paycheck(self):
        print(self.name)
        print(self.remunerationStrategy.details())
        print("This paycheck amount: $%d" % self.remunerationStrategy.paycheckAmount())

if __name__ == "__main__":
    Employee("John Doe", SalaryStrategy(100000)).paycheck()
    Employee("Frank", SalaryStrategy(50000)).paycheck()
    Employee("Joe", HourlyRateStrategy(45)).paycheck()
    Employee("Helen", HourlyRateStrategy(90)).paycheck()
