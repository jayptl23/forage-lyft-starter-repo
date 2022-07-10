from battery.battery import Battery
from engine import Engine
from serviceable import Serviceable
from tires import Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
