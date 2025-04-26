import re

# Keywords for stopping the chatbot
KEY_WORDS_STOP = ['exit', 'stop', 'quit', 'bye', 'goodbye', 'no']

# Categories for travel reasons
REASONS = {
    "adventure": ["hiking", "skiing", "surfing", "climbing"],
    "relaxation": ["spa", "beach", "resort", "retreat"],
    "culture": ["museum", "history", "art", "architecture"],
    "food": ["cuisine", "dining", "street food", "gourmet"]
}

# Climate preferences
CLIMATES = ["warm", "cold", "tropical", "mild"]

# Budget ranges
BUDGET_STATEMENT = {
    "under $1000": "Budget-friendly options!",
    "between $1000 and $3000": "A solid mid-range budget!",
    "over $3000": "Luxury travel is on the table!"
}

# Main chatbot function
def chatbot():
    """
    This function serves as the main entry point for the chatbot.
    It interacts with the user, processes their input, and provides travel recommendations.
    """
    printGreeting()
    while True:
        # Prompt the user for input and provide examples of what they can ask
        user_input = input(
            "How can I assist you today? Here are some examples of what you can ask:\n"
            "- 'Where should I travel?'\n"
            "- 'What are some budget-friendly destinations?'\n"
            "- 'Can you recommend a warm climate destination?'\n"
            "- 'I want to go hiking. Where should I go?'\n"
            "Type 'stop' at any time to exit.\n"
            "Your question: ").lower().strip()

        # Check for exit keywords
        if checkForExitWords(user_input):
            printExit()
            break
        # Handle travel-related queries
        elif "where should i travel" in user_input:
            processTravelChat()
        elif "budget-friendly" in user_input:
            print("I can help you find destinations within your budget. Let's start by understanding the purpose of your travel.")
            processTravelChat()
        elif "warm climate" in user_input:
            print("I can recommend destinations with a warm climate. Let's start by understanding the purpose of your travel.")
            processTravelChat()
        elif "hiking" in user_input:
            print("I can suggest great hiking destinations. Let's start by understanding the purpose of your travel.")
            processTravelChat()
        # Handle unrecognized input
        else:
            printErrorProcessing(user_input)

# Process travel chat
def processTravelChat():
    """
    This function handles the travel recommendation process.
    It collects the user's preferences for travel purpose, budget, and climate,
    and provides tailored recommendations based on their input.
    """
    while True:
        # Ask for the purpose of travel
        reason_response = input("What is the purpose of your travel? (e.g., hiking, relaxation, food) ").lower().strip()
        if checkForExitWords(reason_response):
            printExit()
            break
        reason, reason_value = processReason(reason_response)
        if reason is None:
            printErrorProcessing(reason_response)
            continue

        # Ask for the user's budget
        budget_response = input("What is your approximate budget? (e.g., $500, $1500, $5000) ").lower().strip()
        if checkForExitWords(budget_response):
            printExit()
            break
        budget, budget_value = processBudget(budget_response)
        if budget is None:
            printErrorProcessing(budget_response)
            continue

        # Ask for the preferred climate
        climate_response = input("What is your preferred climate? (e.g., warm, cold, tropical) ").lower().strip()
        if checkForExitWords(climate_response):
            printExit()
            break
        climate = processClimate(climate_response)
        if climate is None:
            printErrorProcessing(climate_response)
            continue

        # Provide a recommendation based on the collected inputs
        destination = processRecommendation(reason, reason_value, budget, budget_value, climate)
        if destination:
            print(f"For {reason} in a {climate} climate with a budget of {budget_value}, I recommend {destination}.")
        else:
            print(f"Sorry, I couldn't find a destination for {reason} in a {climate} climate with a budget of {budget_value}.")
        break

# Process reason for travel
def processReason(reason_input):
    """
    Identifies the user's reason for travel based on their input.
    Returns the reason category and the specific keyword matched.
    """
    for reason, keywords in REASONS.items():
        for keyword in keywords:
            if keyword in reason_input:
                return reason, keyword
    return None, None

# Process budget
def processBudget(budget_response):
    """
    Extracts the user's budget from their input and categorizes it into predefined ranges.
    Returns the budget category and the numeric value.
    """
    match = re.search(r"[0-9]+[.]?[0-9]*", budget_response)
    if match:
        budget_number = float(match.group())
        if budget_number < 1000:
            return "under $1000", budget_number
        elif budget_number < 3000:
            return "between $1000 and $3000", budget_number
        else:
            return "over $3000", budget_number
    return None, None

# Process climate preference
def processClimate(climate_response):
    """
    Validates the user's climate preference against predefined options.
    Returns the climate if valid, otherwise None.
    """
    return climate_response if climate_response in CLIMATES else None

# Provide recommendations based on inputs
def processRecommendation(reason, reason_value, budget, budget_value, climate):
    """
    Provides tailored travel recommendations based on the user's reason for travel,
    budget, and climate preference. Uses nested conditionals and ternary operators
    to streamline the logic.
    """
    if reason == "food":
        if reason_value == "cuisine":
            return "Paris, France" if budget == "over $3000" else "New Orleans, USA"
        elif reason_value == "street food":
            return "Bangkok, Thailand" if climate == "warm" else "Portland, USA"
    elif reason == "adventure":
        if climate == "cold":
            return "Swiss Alps" if budget == "over $3000" else "Aspen, USA"
        elif climate == "warm":
            return "Hawaii" if budget == "between $1000 and $3000" else "Costa Rica"
    elif reason == "relaxation":
        return "Maldives" if budget == "over $3000" else "Bali, Indonesia"
    elif reason == "culture":
        return "Kyoto, Japan" if climate == "mild" else "Rome, Italy"
    return None

# Check for exit keywords
def checkForExitWords(user_input):
    """
    Checks if the user's input contains any keywords indicating they want to exit the chatbot.
    """
    return user_input in KEY_WORDS_STOP

# Print error message
def printErrorProcessing(input):
    """
    Prints an error message when the user's input cannot be processed.
    """
    print(f"I didn't understand '{input}'. Please try again or type 'stop' to exit.")

# Print greeting
def printGreeting():
    """
    Prints a greeting message when the chatbot starts.
    """
    print("Welcome to the Travel Chatbot!")
    print("I can help you find travel destinations based on your preferences.")
    print("Type 'stop' at any time to exit.")

# Print exit message
def printExit():
    """
    Prints a goodbye message when the user exits the chatbot.
    """
    print("Goodbye! Have a great trip!")

# Entry point
if __name__ == "__main__":
    chatbot()