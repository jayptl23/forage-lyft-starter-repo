from battery import Battery
from datetime import date
from utils import get_service_threshold_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = get_service_threshold_date(
            self.last_service_date, 4)
        return service_threshold_date < self.current_date
