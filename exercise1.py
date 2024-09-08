class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors} doors"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return f"{super().display_info()}, Payload Capacity: {self.payload_capacity} lbs"

# Creating instances of the classes
vehicle = Vehicle("Generic", "Vehicle", 1731)
car = Car("Toyota", "Corolla", 1731, 4)
truck = Truck("Ford", "F-150", 1731, 2000)

# Displaying information for each vehicle
print(vehicle.display_info())
print(car.display_info())
print(truck.display_info())
