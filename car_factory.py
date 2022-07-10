from datetime import date
from typing import List
from battery import NubbinBattery, SpindlerBattery
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from tires import Carrigan, Octoprime


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
