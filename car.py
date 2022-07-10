from abc import ABC, abstractmethod
from datetime import date
from typing import List
from battery import Battery, NubbinBattery, SpindlerBattery
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine
from tires import Tires, Carrigan, Octoprime


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[int]) -> Car:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tire_wear)
        return Car(capulet_engine, spindler_battery, tires)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[int]) -> Car:
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tire_wear)
        return Car(willoughby_engine, spindler_battery, tires)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: List[int]) -> Car:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tire_wear)
        return Car(sternman_engine, spindler_battery, tires)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[int]) -> Car:
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprime(tire_wear)
        return Car(willoughby_engine, nubbin_battery, tires)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[int]) -> Car:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprime(tire_wear)
        return Car(capulet_engine, nubbin_battery, tires)
