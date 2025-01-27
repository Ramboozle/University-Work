# Prompt the user to enter their name, and respond with a cheery greeting that includes the name. - Done
# Display the agent's name to the user (this will be a randomly generated name, perhaps chosen from a list). - Done
# Allow the user to enter questions, with no response. - Done
# Exit when the user enters bye. - Done

# 1. Detect at least *four* key words in the user's question, and respond accordingly. - Done
# 2. Print a random response if a key word is not found. - Done
# 3. Include the user's name in some of the responses. - Done
# 4. Exit if the user enters ``quit``, ``exit`` (or any similar string). - Done

import random
Names = ["Mike","Sara","Steve","Clare","Alina","John","Linda","Tom","Freya","Oliver","Ram"]
AgentName = random.choice(Names)
UsersName = input("What is your name? ").strip()
print(f"Hello {UsersName}! My name is {AgentName}. How can I help you today?")
while True:
    UserInput = input()
    if UserInput.lower() == "bye" or UserInput == "quit" or UserInput == "exit":
        print(f"See you later {UsersName}!")
        break

    if "weather" in UserInput.lower() or "outside" in UserInput.lower() or "temperature" in UserInput.lower():
        print(f"The weather is nice today on campus! I'd recommend wearing a light jacket {UsersName}.")
        print(f"Is there anything else I can help you with {UsersName}?")
    elif "food" in UserInput.lower() or "cafeteria" in UserInput.lower() or "lunch" in UserInput.lower():
        print(f"I'd recommend trying the new sandwich at the cafeteria {UsersName}.")
        print(f"Is there anything else I can help you with {UsersName}?")
    elif "library" in UserInput.lower():
        print(f"The library is open until 10pm today {UsersName}. Make sure to bring your student ID.")
        print(f"Is there anything else I can help you with {UsersName}?")
    elif "parking" in UserInput.lower() or "car" in UserInput.lower():
        print(f"The parking lot is full today {UsersName}. I'd recommend parking on the street.")
        print(f"Is there anything else I can help you with {UsersName}?")
    else:
        print("I'm sorry, I don't understand. Can you please rephrase your question?")