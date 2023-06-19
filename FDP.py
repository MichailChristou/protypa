from abc import ABC, abstractmethod

# Product
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete Products
class Sedan(Car):
    def drive(self):
        print("Driving a Sedan")

class SUV(Car):
    def drive(self):
        print("Driving an SUV")

# Factory
class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Invalid car type")

# Usage
car_factory = CarFactory()

sedan = car_factory.create_car("sedan")
sedan.drive()  # Output: Driving a Sedan

suv = car_factory.create_car("suv")
suv.drive()  # Output: Driving an SUV
