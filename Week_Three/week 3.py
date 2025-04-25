'''
ITEC5025 Week 3 Example Code
This source file includes example code to illustrate the principle concepts needed for Week 3 assignment
This source code may also include methods and techinques demonstrated from previous assignments
NOTE: You are permitted to use AI code generation sources to assist with the assignment
IF YOU USE AI CODE GENERATION SOURCES, YOU MUST CITE THE AI ASSISTANT USED IN EITHER:
- an accompanying report document
- within a comment / header block with the source file being submitted

Objective:
- utilize if/else flow control
    - REQUIRED if, elif, and else
- utilize nested conditionals to branch  based on multiple criteria
- utilize else fallbacks to handle default responses, ask for more input, fallback responses
- utilize Ternary operator for conditionals returning between two values

'''
# import packages and modules needed for additional functionality #
import re

# This is a list used to store specific 'KEY WORDS' Using a list makes it easy to check if a token matches any value in the list #
KEY_WORDS_STOP = ['exit', 'stop', 'quit', 'bye', 'goodbye', 'no']

REASONS = {
    "activities": ["sports", "hiking", "skiing", "swimming", "water", "fishing"],
    "relaxation": ["leisure", "relax", "rest", "calm", "peace", "quiet", "privacy"],
    "culture": ["city", "tour", "attraction", "sight", "culture", "atmosphere", "people"],
    "food": ["food", "pasta", "sushi", "tacos", "seafood", "cuisine", "eat", "taste"]
}

REASON_STATEMENT = {
    "activities":"Very adventurous!",
    "relaxation":"You deserve a break!",
    "culture":"How exciting!",
    "food":"Delicious!"
}

BUDGET_STATEMENT = {
    "under $1000":"Looking at small excursions!",
    "between $1000 and $3000":"A solig budget",
    "over 3000":"Luxury options are on the table!"
}

# This function performs the main input and process loop
# it prompts for a user input and then passes that input through various types of processing
# if the input wasn't accepted by any of the processing functions, the user is asked to 'rephrase' their prompt
def processRequests():
    while True:
        # get input from user #
        user_input = input("Would you like assistance with travel recommendations? ").lower().strip()
        
        if checkForExitWords(user_input):
            printExit()
            exit(0)
        # process travel statements #
        elif user_input == "yes" or user_input == "y":
            processTravelChat()
        else:
            printErrorProcessing(user_input)

# This function will process user input to try to obtain three pieces of information
# reason for travel (activities, relaxation, culture, food)
# budget ($1000 or less, $1000 - $3000, more than $3000)
def processTravelChat():
    while True:
        reason_response = input("What is the purpose of your travel?\nFor example, are you interested in skiing, relaxation, sight seeing, or food tasting? ").lower().strip()
        if checkForExitWords(reason_response):
            exit(0)
        reason, reason_value = processReason(reason_response)
        if reason == None:
            printErrorProcessing(reason_response)
        else:
            print (f"You are traveling for {reason}, {REASON_STATEMENT[reason]}")
            budget_response = input("What is your approximate budget?\n For example, $500, 1050.55, $5555.55?").lower().strip()
            if checkForExitWords(budget_response):
                exit(0)
            budget, budget_value = processBudget(budget_response)
            if budget == None:
                printErrorProcessing(budget_response)
            else:
                print(f"Your budget is ${budget}, {BUDGET_STATEMENT[budget]}")
                destination = processRecommendation(reason, reason_value, budget, budget_value)
                if destination != None:
                    print(f"For {reason} with a budget of ${budget_value}, I recommend {destination}")
                else:
                    print(f"I am sorry, I couldn't find any destinations for {reason} on a budget of ${budget_value}")
                #exit(0)

# this function takes in the reason and budget and provides recommendations
def processRecommendation(reason:str, reason_value:str, budget:str, budget_value:float):
    if reason == "food":
        if reason_value == "sushi":
            return "Gulf Shores" if budget == "under $1000" else "Nara, Japan"
        elif reason_value == "pasta":
            return "Olive Garden" if budget == "under $1000" else "New York" if budget == "between $1000 and $3000" else "Venice, Italy"
        else:
            return "USA"
    
    # TODO EXPAND OPTION STATES
    return None

# This function performs a simple loop over the input
# it checks if any key words for any of the reasons exist in the input
# if so, take the matched reason, otherwise return None
def processReason(reason_input:str):
    # iterate of the reasons
    for reason in REASONS:
        # iterate over each key word in the selected reason and see if there's a match
        for keyword in REASONS[reason]:
            if keyword in reason_input:
                return reason, keyword
    return None, None
            
# this function performs a simple regex to extract number
# it then checks the number to be within three ranges and retiurns the range it falls into
def processBudget(budget_response):
    # process for number block #
    number = r"[0-9]+[.]?[0-9]*" 
    # see if any sub part of the input matches the regular expression #
    match = re.search(number, budget_response)
    if match != None:
        # determine the range #
        budget_number = float(match.group())
        
        if budget_number < 1000:
            return "under $1000", budget_number
        elif budget_number < 3000:
            return "between $1000 and $3000", budget_number
        else:
            return "over 3000", budget_number
    return None, None


# check for exit keywords #
def checkForExitWords(user_input):
    # check for exit key word(s) #
    return user_input in KEY_WORDS_STOP

# simple print statement asking to rephrase
def printErrorProcessing(input: str):
    print(f"I am sorry, I did not understand the request\n'{input}'\nPlease rephrase your request.")
    printExample()


# can be used to reprint examples
def printExample():
    print("To end the chat session, simply type 'stop'")


# prints goodbye message
def printExit():
    print("Goodbye!")


# This function performs a simple greeting print
# it could be used to provide some examples up front of the kinds of prompts the chatbot is able to support
def printGreeting():    
    print("Hello, this chatbot is able to assist with providing basic travel recommendations.")
    printExample()


def chatbot():
    printGreeting()
    processRequests()


# entry point of main function #
chatbot()