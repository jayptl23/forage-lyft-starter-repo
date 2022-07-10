from typing import List
from tires import Tires


class Octoprime(Tires):
    def __init__(self, tire_wear: List[int]):
        self.tire_wear = tire_wear

    def needs_service(self):
        tire_wear_sum = 0
        for wear in self.tire_wear:
            tire_wear_sum += wear
        return tire_wear_sum >= 3
