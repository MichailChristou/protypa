from abc import ABC, abstractmethod

# Abstract Products
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class Tires(ABC):
    @abstractmethod
    def rotate(self):
        pass

# Concrete Products
class V6Engine(Engine):
    def start(self):
        print("Starting V6 Engine")

class V8Engine(Engine):
    def start(self):
        print("Starting V8 Engine")

class SummerTires(Tires):
    def rotate(self):
        print("Rotating Summer Tires")

class WinterTires(Tires):
    def rotate(self):
        print("Rotating Winter Tires")

# Abstract Factory
class CarFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_tires(self):
        pass

# Concrete Factories
class SedanFactory(CarFactory):
    def create_engine(self):
        return V6Engine()

    def create_tires(self):
        return SummerTires()

class SUVFactory(CarFactory):
    def create_engine(self):
        return V8Engine()

    def create_tires(self):
        return WinterTires()

# Usage
sedan_factory = SedanFactory()
sedan_engine = sedan_factory.create_engine()
sedan_tires = sedan_factory.create_tires()

sedan_engine.start()  # Output: Starting V6 Engine
sedan_tires.rotate()  # Output: Rotating Summer Tires

suv_factory = SUVFactory()
suv_engine = suv_factory.create_engine()
suv_tires = suv_factory.create_tires()

suv_engine.start()  # Output: Starting V8 Engine
suv_tires.rotate()  # Output: Rotating Winter Tires
