from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")

    def fuel_type(self):
        print("Petrol")
class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def fuel_type(self):
        print("Petrol")

class Tesla(Vehicle):
    def start(self):
        print("Tesla started")

    def fuel_type(self):
        print("Electric")

c = Car()
b = Bike()
t = Tesla()

c.start()
c.fuel_type()

b.start()
b.fuel_type()

t.start()
t.fuel_type()