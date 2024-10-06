# Design patterns using simple-factory.

from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC):
    @abstractmethod
    def get_client(self) -> None: pass


class PopularVehicle(Vehicle):
    def get_client(self) -> None:
        print("The popular vehicle is wainting for the client")


class LuxuryVehicle(Vehicle):
    def get_client(self) -> None:
        print("The luxury vehicle is waiting for the client")


class PopularMotorcycle(Vehicle):
    def get_client(self) -> None:
        print("The Popular motorcycle is waiting for the client")


class LuxuryMotorcycle(Vehicle):
    def get_client(self):
        print("The luxury motorcycle is waiting for the client")


class FactoryVehicle:
    def __init__(self, type):
        self.vehicle = self.get_vehicle(type)

    @staticmethod
    def get_vehicle(tipo: str) -> Vehicle:
        if tipo == 'Luxury':
            return LuxuryVehicle()
        if tipo == 'Popular':
            return PopularVehicle()
        if tipo == 'Motorcycle':
            return PopularMotorcycle()
        if tipo == 'Luxury_motorcycle':
            return LuxuryMotorcycle()
        assert 0, 'There is not vehicle'

        def get_client(self):
            self.vehicle.get_client()


if __name__ == '__main__':
    vehicle_available = ['Luxury', 'Popular',
                         'Motorcycle', 'Luxury_motorcycle']

    for i in range(10):
        car = FactoryVehicle(choice(vehicle_available))
        car.get_client()
