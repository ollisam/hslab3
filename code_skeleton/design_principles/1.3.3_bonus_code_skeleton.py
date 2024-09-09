from dataclasses import dataclass
from enum import Enum
from typing import List
from abc import ABC, abstractmethod


class ShipmentType(Enum):
    plane = 0
    ship = 1
    car = 2
    carrier_pigeon = 3


@dataclass
class Size:
    width: float
    height: float
    weight: float


@dataclass
class Product:
    name: str
    price: float
    size: Size


@dataclass
class Address:
    country: str
    street_address: str
    city: str
    zip_code: int


@dataclass
class Person:
    name: str
    ssn: str
    address: Address


@dataclass
class Package:
    shipment_type: ShipmentType
    product: Product
    merchant: Person
    buyer: Person


class Transport(ABC):
    @abstractmethod
    def ship(self, package: Package):
        pass


class Ship(Transport):
    def reload_fuel_oil(self):
        print('reloading fuel supplies on ship')

    def ship(self, package: Package):
        self.reload_fuel_oil()
        print(f'shipping package via ship from {package.merchant.address} to {package.buyer.address}')


class Plane(Transport):
    def reload_jet_fuel(self):
        print("jet fuels can't melt steel beams")

    def ship(self, package: Package):
        self.reload_jet_fuel()
        print(f'flying package from {package.merchant.address} to {package.buyer.address}')


class Car(Transport):
    def reload_gas(self):
        print('adding gasoline... or diesel')

    def ship(self, package: Package):
        self.reload_gas()
        print(f'driving package from {package.merchant.address} to {package.buyer.address}')


class CarrierPigeon(Transport):
    def eat_seeds(self):
        print("beep beep I'm a bird")

    def ship(self, package: Package):
        self.eat_seeds()
        print(f'beep beep I\'m a bird, flying package from {package.merchant.address} to {package.buyer.address}')


class ShipmentService:
    def ship(self, transport: Transport, package: Package):
        transport.ship(package)