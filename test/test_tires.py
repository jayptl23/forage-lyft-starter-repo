import unittest
from tires import Carrigan
from tires import Octoprime


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = Carrigan([0.3, 0.2, 0.7, 0.9])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires = Carrigan([0, 0.5, 0, 0.8])
        self.assertFalse(tires.needs_service())


class TestOctoPrimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = Octoprime([1, 1, 0.8, 0.2])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires = Octoprime([0, 0, 1, 1])
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
