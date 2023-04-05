import pytest
from App.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 0, 17) == 0

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 12, 3) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 500, 300) == 200

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 115, 50) == 165