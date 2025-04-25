import unittest
from unittest.mock import patch
from week2 import processArithmetic, processPhrases, printErrorProcessing, printExit

class TestWeek2(unittest.TestCase):

    def test_processArithmetic(self):
        # Test valid arithmetic inputs
        self.assertTrue(processArithmetic("5 + 3"))  # Addition
        self.assertTrue(processArithmetic("10 - 4"))  # Subtraction
        self.assertTrue(processArithmetic("6 * 7"))  # Multiplication
        self.assertTrue(processArithmetic("8 / 2"))  # Division

        # Test invalid arithmetic inputs
        self.assertFalse(processArithmetic("5 + "))  # Incomplete input
        self.assertFalse(processArithmetic("hello + world"))  # Non-numeric input
        self.assertFalse(processArithmetic("8 / 0"))  # Division by zero handled in output, but still valid syntax

    @patch('builtins.print')
    def test_processArithmetic_output(self, mock_print):
        # Test output for valid addition
        processArithmetic("5 + 3")
        mock_print.assert_called_with("The result of 5.0 + 3.0 is 8.0")

        # Test output for valid subtraction
        processArithmetic("10 - 4")
        mock_print.assert_called_with("The result of 10.0 - 4.0 is 6.0")

        # Test output for valid multiplication
        processArithmetic("6 * 7")
        mock_print.assert_called_with("The result of 6.0 * 7.0 is 42.0")

        # Test output for valid division
        processArithmetic("8 / 2")
        mock_print.assert_called_with("The result of 8.0 / 2.0 is 4.0")

        # Test output for division by zero
        processArithmetic("8 / 0")
        mock_print.assert_called_with("Error: Division by zero is not allowed.")

    @patch('builtins.print')
    def test_processPhrases(self, mock_print):
        # Test "greater than" phrase
        self.assertTrue(processPhrases("5 greater than 3"))
        mock_print.assert_called_with("Yes, 5.0 is greater than 3.0.")

        self.assertTrue(processPhrases("2 greater than 5"))
        mock_print.assert_called_with("No, 2.0 is not greater than 5.0.")

        # Test "less than" phrase
        self.assertTrue(processPhrases("3 less than 5"))
        mock_print.assert_called_with("Yes, 3.0 is less than 5.0.")

        self.assertTrue(processPhrases("10 less than 5"))
        mock_print.assert_called_with("No, 10.0 is not less than 5.0.")

        # Test "equal to" phrase
        self.assertTrue(processPhrases("5 equal to 5"))
        mock_print.assert_called_with("Yes, 5.0 is equal to 5.0.")

        self.assertTrue(processPhrases("-1 equal to 10"))
        mock_print.assert_called_with("No, -1.0 is not equal to 10.0.")

        # Test "not equal to" phrase
        self.assertTrue(processPhrases("5 not equal to 3"))
        mock_print.assert_called_with("Yes, 5.0 is not equal to 3.0.")

        self.assertTrue(processPhrases("5 not equal to 5"))
        mock_print.assert_called_with("No, 5.0 is equal to 5.0.")

        # Test "who is older" phrase
        self.assertTrue(processPhrases("Who is older if 1990 and 2000?"))
        mock_print.assert_called_with("The person born in 1990 is older than the person born in 2000.")

        self.assertTrue(processPhrases("Who is older if 2000 and 1990?"))
        mock_print.assert_called_with("The person born in 1990 is older than the person born in 2000.")

        self.assertTrue(processPhrases("Who is older if 1990 and 1990?"))
        mock_print.assert_called_with("Both were born in 1990, so they are the same age.")

        # Test "users born after X and have Y hair" phrase
        self.assertTrue(processPhrases("users born after 2000 and have red hair"))
        mock_print.assert_called_with("Users born after 2000 and have red hair: Diana.")

        self.assertTrue(processPhrases("users born after 2010 and have red hair"))
        mock_print.assert_called_with("No users born after 2010 and have red hair.")

        # Test "users born before X or have Y eyes" phrase
        self.assertTrue(processPhrases("users born before 1990 or have blue eyes"))
        mock_print.assert_called_with("Users born before 1990 or have blue eyes: Alice, Charlie.")

        self.assertTrue(processPhrases("users born before 1980 or have green eyes"))
        mock_print.assert_called_with("Users born before 1980 or have green eyes: Bob.")

        # Test invalid phrase
        self.assertFalse(processPhrases("Is this a valid phrase?"))

    @patch('builtins.print')
    def test_printErrorProcessing(self, mock_print):
        # Test error message output
        printErrorProcessing("invalid input")
        mock_print.assert_any_call("I am sorry, I did not understand the request\n'invalid input'\nPlease rephrase your request.")

    @patch('builtins.print')
    def test_printExit(self, mock_print):
        # Test goodbye message
        printExit()
        mock_print.assert_called_with("Goodbye!")

if __name__ == '__main__':
    unittest.main()