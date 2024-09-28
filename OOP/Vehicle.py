class Vehicle:
    def __init__(self, year, odometer):
        self.year = year
        self.odometer = odometer

    def __str__(self):
        return f" year: {self.year} \n odometer: {self.odometer}"

class Car(Vehicle):
    def __init__(self, year, odometer, brand):
        super().__init__(year, odometer)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f"\n brand {self.brand}"

x = Car(1992, 5000, "VOLVO")
print(x)
