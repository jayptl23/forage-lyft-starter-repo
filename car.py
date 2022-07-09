from abc import ABC, abstractmethod
from datetime import date
from battery import Battery, NubbinBattery, SpindlerBattery
from engine import Engine, CapuletEngine, SternmanEngine, WilloughbyEngine


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(capulet_engine, spindler_battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(sternman_engine, spindler_battery)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(willoughby_engine, nubbin_battery)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(capulet_engine, nubbin_battery)
