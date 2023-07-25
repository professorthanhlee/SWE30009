# Temperature Conversion Test Program
# Developer: [Le Nam Cong Thanh]
# Student ID: [103410217]
import random
from unittest.mock import patch
from converter import main, celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit
import unittest


class TestSymmetryRelation(unittest.TestCase):
    # MR1 - Symmetry Relation Test Cases

    def test_symmetry_relation1(self):
        # Test Case 1: C -> F -> C
        si = random.uniform(-1000, 1000)
        so = celsius_to_fahrenheit(si)
        fi = so
        with patch('builtins.input', side_effect=['2', str(fi)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi:.2f} degrees Fahrenheit is equal to {si:.2f} degrees Celsius.")

    def test_symmetry_relation2(self):
        # Test Case 2: C -> K -> C
        si_1 = random.uniform(-1000, 1000)
        so_1 = celsius_to_kelvin(si_1)
        fi_1 = so_1
        with patch('builtins.input', side_effect=['4', str(fi_1)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi_1:.2f} Kelvin is equal to {si_1:.2f} degrees Celsius.")

    def test_symmetry_relation3(self):
        # Test Case 3: F -> C -> F
        si_2 = random.uniform(-1000, 1000)
        so_2 = fahrenheit_to_celsius(si_2)
        fi_2 = so_2
        with patch('builtins.input', side_effect=['1', str(fi_2)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi_2:.2f} degrees Celsius is equal to {si_2:.2f} degrees Fahrenheit.")
    # MR2 - Composition Relation Test Cases

    def test_composition_relation1(self):
        # Test Case 1: C -> F = C -> K -> F
        si = random.uniform(-1000, 1000)
        so = celsius_to_fahrenheit(si)
        fi = si
        fo = celsius_to_kelvin(fi)
        fi_1 = fo
        with patch('builtins.input', side_effect=['6', str(fi_1)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi_1:.2f} Kelvin is equal to {so:.2f} degrees Fahrenheit.")

    def test_composition_relation2(self):
        # Test Case 2: C -> K = C -> F -> K
        si_1 = random.uniform(-1000, 1000)
        so_1 = celsius_to_kelvin(si_1)
        fi_2 = si_1
        fo_2 = celsius_to_fahrenheit(fi_2)
        fi_3 = fo_2
        with patch('builtins.input', side_effect=['5', str(fi_3)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi_3:.2f} degrees Fahrenheit is equal to {so_1:.2f} Kelvin.")

    def test_composition_relation3(self):
        # Test Case 3: F -> K = F -> C -> K
        si_2 = random.uniform(-1000, 1000)
        so_2 = fahrenheit_to_kelvin(si_2)
        fi_3 = si_2
        fo_3 = fahrenheit_to_celsius(fi_3)
        fi_4 = fo_3
        with patch('builtins.input', side_effect=['3', str(fi_4)]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"{fi_4:.2f} degrees Celsius is equal to {so_2:.2f} Kelvin.")

    def test_input_user(self):
        input = not random.uniform(1, 6)
        with patch('builtins.input', side_effect=[input]):
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called_with(
                    f"Invalid choice. Please select a valid option (1/2/3/4/5/6).")


if __name__ == '__main__':
    unittest.main()
