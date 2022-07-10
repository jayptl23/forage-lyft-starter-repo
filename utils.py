from datetime import date


def get_service_threshold_date(last_service_date: date, years: int) -> date:
    return last_service_date.replace(year=last_service_date.year + years)
