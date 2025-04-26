import unittest
from unittest.mock import patch
from week3 import (
    processReason,
    processBudget,
    processClimate,
    processRecommendation,
    checkForExitWords,
    printErrorProcessing,
    printGreeting,
    printExit,
)

class TestChatbot(unittest.TestCase):
    """
    Unit tests for the chatbot functions in week3.py.
    """

    def test_processReason(self):
        """
        Test the processReason function to ensure it correctly identifies
        the user's reason for travel based on input.
        """
        # Test valid reasons
        self.assertEqual(processReason("I want to go hiking"), ("adventure", "hiking"))
        self.assertEqual(processReason("I love museums"), ("culture", "museum"))
        self.assertEqual(processReason("I want to relax at a spa"), ("relaxation", "spa"))
        self.assertEqual(processReason("I enjoy street food"), ("food", "street food"))

        # Test invalid reason
        self.assertEqual(processReason("I want to do something else"), (None, None))

    def test_processBudget(self):
        """
        Test the processBudget function to ensure it correctly extracts
        and categorizes the user's budget.
        """
        # Test valid budgets
        self.assertEqual(processBudget("$500"), ("under $1000", 500.0))
        self.assertEqual(processBudget("$1500"), ("between $1000 and $3000", 1500.0))
        self.assertEqual(processBudget("$5000"), ("over $3000", 5000.0))

        # Test invalid budget
        self.assertEqual(processBudget("no budget"), (None, None))

    def test_processClimate(self):
        """
        Test the processClimate function to ensure it validates the user's
        climate preference correctly.
        """
        # Test valid climates
        self.assertEqual(processClimate("warm"), "warm")
        self.assertEqual(processClimate("cold"), "cold")
        self.assertEqual(processClimate("tropical"), "tropical")
        self.assertEqual(processClimate("mild"), "mild")

        # Test invalid climate
        self.assertIsNone(processClimate("rainy"))

    def test_processRecommendation(self):
        """
        Test the processRecommendation function to ensure it provides
        tailored travel recommendations based on user inputs.
        """
        # Test recommendations for food
        self.assertEqual(processRecommendation("food", "cuisine", "over $3000", 4000, "warm"), "Paris, France")
        self.assertEqual(processRecommendation("food", "street food", "under $1000", 800, "warm"), "Bangkok, Thailand")

        # Test recommendations for adventure
        self.assertEqual(processRecommendation("adventure", "hiking", "over $3000", 4000, "cold"), "Swiss Alps")
        self.assertEqual(processRecommendation("adventure", "hiking", "under $1000", 800, "warm"), "Costa Rica")

        # Test recommendations for relaxation
        self.assertEqual(processRecommendation("relaxation", "spa", "over $3000", 4000, "warm"), "Maldives")
        self.assertEqual(processRecommendation("relaxation", "spa", "under $1000", 800, "warm"), "Bali, Indonesia")

        # Test recommendations for culture
        self.assertEqual(processRecommendation("culture", "museum", "over $3000", 4000, "mild"), "Kyoto, Japan")
        self.assertEqual(processRecommendation("culture", "museum", "under $1000", 800, "cold"), "Rome, Italy")

        # Test no recommendation
        self.assertIsNone(processRecommendation("unknown", "unknown", "under $1000", 800, "warm"))

    def test_checkForExitWords(self):
        """
        Test the checkForExitWords function to ensure it correctly identifies
        exit keywords and non-exit keywords.
        """
        # Test exit keywords
        self.assertTrue(checkForExitWords("stop"))
        self.assertTrue(checkForExitWords("exit"))
        self.assertTrue(checkForExitWords("quit"))
        self.assertTrue(checkForExitWords("bye"))
        self.assertTrue(checkForExitWords("goodbye"))

        # Test non-exit keywords
        self.assertFalse(checkForExitWords("hello"))
        self.assertFalse(checkForExitWords("travel"))

    @patch('builtins.print')
    def test_printErrorProcessing(self, mock_print):
        """
        Test the printErrorProcessing function to ensure it prints the correct
        error message when the user's input cannot be processed.
        """
        printErrorProcessing("invalid input")
        mock_print.assert_called_with("I didn't understand 'invalid input'. Please try again or type 'stop' to exit.")

    @patch('builtins.print')
    def test_printGreeting(self, mock_print):
        """
        Test the printGreeting function to ensure it prints the correct
        greeting message when the chatbot starts.
        """
        printGreeting()
        mock_print.assert_any_call("Welcome to the Travel Chatbot!")
        mock_print.assert_any_call("I can help you find travel destinations based on your preferences.")
        mock_print.assert_any_call("Type 'stop' at any time to exit.")

    @patch('builtins.print')
    def test_printExit(self, mock_print):
        """
        Test the printExit function to ensure it prints the correct
        exit message when the user exits the chatbot.
        """
        printExit()
        mock_print.assert_called_with("Goodbye! Have a great trip!")

if __name__ == "__main__":
    unittest.main()