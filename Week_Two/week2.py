# This is a simple chatbot that can perform basic arithmetic operations and respond to natural language queries
# It uses regular expressions to parse user input and determine the appropriate response
# The chatbot can handle addition, subtraction, multiplication, and division
# It can also respond to phrases like "Is X greater than Y", "Is X less than Y", and "Is X equal to Y"
# The chatbot will continue to prompt the user for input until the user types a specific exit command
# The chatbot is designed to be user-friendly and provide clear feedback on the operations performed
# Importing the regular expression module to handle string pattern matching
# This module provides support for regular expressions in Python
# It allows us to search for specific patterns in strings, which is useful for parsing user input
# Importing the regular expression module
# This module provides support for regular expressions in Python
# It allows us to search for specific patterns in strings, which is useful for parsing user input
import re

# This is a list used to store specific 'KEY WORDS' Using a list makes it easy to check if a token matches any value in the list #
KEY_WORDS_STOP = ['exit', 'stop', 'quit', 'bye', 'goodbye']

# This function performs the main input and process loop
# it prompts for a user input and then passes that input through various types of processing
# if the input wasn't accepted by any of the processing functions, the user is asked to 'rephrase' their prompt
def processRequests():
    while True:
        # get input from user #
        user_input = input("How may I assist you? ").lower().strip()
        # check for exit key word(s) #
        if user_input in KEY_WORDS_STOP:
            printExit()
            break
        # process arithmetic tokens #
        elif processArithmetic(user_input):
            continue
        # process word statements #
        elif processPhrases(user_input):
            continue
        else:
            printErrorProcessing(user_input)

# This function takes in an input string and applies a regular expression filter to
# extract portions of the input that match specific arithmetic operations
def processArithmetic(input: str):
    # Define patterns for arithmetic operations
    arithmetic_pattern = r"([-]?[0-9]*[.]?[0-9]+)\s*([\+\-\*/])\s*([-]?[0-9]*[.]?[0-9]+)"
    
    # Match the input against the pattern
    arithmetic_match = re.search(arithmetic_pattern, input)
    if arithmetic_match:
        # Extract operands and operator
        left_side = float(arithmetic_match.group(1))
        operator = arithmetic_match.group(2)
        right_side = float(arithmetic_match.group(3))
        
        # Perform the appropriate operation
        if operator == '+':
            result = left_side + right_side
            print(f"The result of {left_side} + {right_side} is {result}")
        elif operator == '-':
            result = left_side - right_side
            print(f"The result of {left_side} - {right_side} is {result}")
        elif operator == '*':
            result = left_side * right_side
            print(f"The result of {left_side} * {right_side} is {result}")
        elif operator == '/':
            if right_side != 0:
                result = left_side / right_side
                print(f"The result of {left_side} / {right_side} is {result}")
            else:
                print("Error: Division by zero is not allowed.")
                return False
        return True

    # If no match, return False
    return False

# hardcoded records for demonstration purposes
USER_RECORDS = [
    {"name": "Alice", "birth_year": 1995, "hair_color": "red", "eye_color": "blue"},
    {"name": "Bob", "birth_year": 2003, "hair_color": "brown", "eye_color": "green"},
    {"name": "Charlie", "birth_year": 1988, "hair_color": "blonde", "eye_color": "blue"},
    {"name": "Diana", "birth_year": 2001, "hair_color": "red", "eye_color": "brown"},
]

# This function takes in an input string and applies a regular expression filter to
# extract portions of the input that match specific arithmetic operations
# This function is used to process phrases that are not strictly arithmetic
# but rather are more natural language statements
# that can be interpreted as arithmetic operations
# For example, "Is 5 greater than 3" or "Is -1 equal to 10"
def processPhrases(input: str):
    # Check for "greater than" phrase
    greater_than_pattern = r"([-]?[0-9]*[.]?[0-9]+)\s*greater\s*than\s*([-]?[0-9]*[.]?[0-9]+)"
    greater_than_match = re.search(greater_than_pattern, input)
    if greater_than_match:
        left_side = float(greater_than_match.group(1))
        right_side = float(greater_than_match.group(2))
        if left_side > right_side:
            print(f"Yes, {left_side} is greater than {right_side}.")
        else:
            print(f"No, {left_side} is not greater than {right_side}.")
        return True

    # Check for "less than" phrase
    less_than_pattern = r"([-]?[0-9]*[.]?[0-9]+)\s*less\s*than\s*([-]?[0-9]*[.]?[0-9]+)"
    less_than_match = re.search(less_than_pattern, input)
    if less_than_match:
        left_side = float(less_than_match.group(1))
        right_side = float(less_than_match.group(2))
        if left_side < right_side:
            print(f"Yes, {left_side} is less than {right_side}.")
        else:
            print(f"No, {left_side} is not less than {right_side}.")
        return True
    
    # Check for "equal to" phrase
    equal_to_pattern = r"([-]?[0-9]*[.]?[0-9]+)\s*equal\s*to\s*([-]?[0-9]*[.]?[0-9]+)"
    equal_to_match = re.search(equal_to_pattern, input)
    if equal_to_match:
        left_side = float(equal_to_match.group(1))
        right_side = float(equal_to_match.group(2))
        if left_side == right_side:
            print(f"Yes, {left_side} is equal to {right_side}.")
        else:
            print(f"No, {left_side} is not equal to {right_side}.")
        return True

    # Check for "not equal to" phrase
    not_equal_to_pattern = r"([-]?[0-9]*[.]?[0-9]+)\s*not\s*equal\s*to\s*([-]?[0-9]*[.]?[0-9]+)"
    not_equal_to_match = re.search(not_equal_to_pattern, input)
    if not_equal_to_match:
        left_side = float(not_equal_to_match.group(1))
        right_side = float(not_equal_to_match.group(2))
        if left_side != right_side:
            print(f"Yes, {left_side} is not equal to {right_side}.")
        else:
            print(f"No, {left_side} is equal to {right_side}.")
        return True

    # Check for "who is older" phrase
    older_pattern = r"who\s*is\s*older\s*if\s*(\d{4})\s*and\s*(\d{4})"
    older_match = re.search(older_pattern, input.lower())
    if older_match:
        year1 = int(older_match.group(1))
        year2 = int(older_match.group(2))
        if year1 < year2:
            print(f"The person born in {year1} is older than the person born in {year2}.")
        elif year1 > year2:
            print(f"The person born in {year2} is older than the person born in {year1}.")
        else:
            print(f"Both were born in {year1}, so they are the same age.")
        return True

    # Check for "users born after X and have Y hair" phrase
    born_after_and_hair_pattern = r"users\s*born\s*after\s*(\d{4})\s*and\s*have\s*(\w+)\s*hair"
    born_after_and_hair_match = re.search(born_after_and_hair_pattern, input)
    if born_after_and_hair_match:
        year = int(born_after_and_hair_match.group(1))
        hair_color = born_after_and_hair_match.group(2).lower()
        matching_users = [
            user["name"]
            for user in USER_RECORDS
            if user["birth_year"] > year and user["hair_color"] == hair_color
        ]
        if matching_users:
            print(f"Users born after {year} and have {hair_color} hair: {', '.join(matching_users)}.")
        else:
            print(f"No users born after {year} and have {hair_color} hair.")
        return True

    # Check for "users born before X or have Y eyes" phrase
    born_before_or_eyes_pattern = r"users\s*born\s*before\s*(\d{4})\s*or\s*have\s*(\w+)\s*eyes"
    born_before_or_eyes_match = re.search(born_before_or_eyes_pattern, input)
    if born_before_or_eyes_match:
        year = int(born_before_or_eyes_match.group(1))
        eye_color = born_before_or_eyes_match.group(2).lower()
        matching_users = [
            user["name"]
            for user in USER_RECORDS
            if user["birth_year"] < year or user["eye_color"] == eye_color
        ]
        if matching_users:
            print(f"Users born before {year} or have {eye_color} eyes: {', '.join(matching_users)}.")
        else:
            print(f"No users born before {year} or have {eye_color} eyes.")
        return True

    # If no match, return False
    return False


# simple print statement asking to rephrase
def printErrorProcessing(input: str):
    print(f"I am sorry, I did not understand the request\n'{input}'\nPlease rephrase your request.")
    printExample()


# can be used to reprint examples
def printExample():
    print("Examples of how I may assist include:")
    print("1. Arithmetic operations:")
    print("   - What is 5 + 6")
    print("   - What is 10 - 4")
    print("   - What is 6 * 7")
    print("   - What is 8 / 2")
    print("2. Comparisons:")
    print("   - Is 5 greater than 3")
    print("   - Is 3 less than 5")
    print("   - Is 5 equal to 5")
    print("   - Is 5 not equal to 3")
    print("3. Age comparisons:")
    print("   - Who is older if 1990 and 2000?")
    print("4. User queries:")
    print("   - Users born after 2000 and have red hair")
    print("   - Users born before 1990 or have blue eyes")
    print("To end the chat session, simply type 'stop'")


# prints goodbye message
def printExit():
    print("Goodbye!")


# This function performs a simple greeting print
# it could be used to provide some examples up front of the kinds of prompts the chatbot is able to support
def printGreeting():    
    print("Hello, this chatbot is able to assist with basic accounting operations.")
    printExample()



def chatbot():
    printGreeting()
    processRequests()


# entry point of main function #
if __name__ == "__main__":
    # entry point of main function #
    chatbot()