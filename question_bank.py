#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.

questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the formula to calculate speed", "s=d/t"),
        ("What is the speed of light", "3x10^8")
    ],
    "Maths": [
        ("What is the formula for Area of Rectangle", "L*B"),
        ("What is the area of triangle", "0.5*(l*b)"),
        ("What is the formula of Pythagoras theorem", "H^2=B^2+P^2")
    ],
    "History": [
        ("Who was the first prime minister of Pakistan", "Liaqat Ali Khan"),
        ("When did Islamabad become the capital of Pakistan", "14 August 1967"),
        ("Who designed the flag of Pakistan", "Amiruddin Kidwai")
    ],
    "Economics": [
        ("What category is involved in business?", "Production"),
        ("What is one aspect of Demand?", "Ability")
    ],
    "Geography": [
        ("Name a land-locked country", "Tajikistan")
    ]
}



hints = {
    "Science": [("Made up of Hydeogen and Oxygen:")
        
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




