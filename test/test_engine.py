import unittest
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(
            current_mileage=60001, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(
            current_mileage=60000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
