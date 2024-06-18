import numpy as np
import pandas as pd
from jupyprint import jupyprint

def esp(correct_guesses):
    zener_cards = np.array(["circle", "cross", "wave", "square", "star"])

    current_card = np.random.choice(zener_cards)

    user_guess = input('Type your guess in the text box: \nChoose one of : "circle", "cross", "wave", "square" or "star"')
    
    user_guess = user_guess.lower()
    
    if user_guess not in zener_cards:
        
        while user_guess not in zener_cards:
            jupyprint("You didn't type the name of a Zener card!")
            user_guess = input('Type your guess below: \nChoose one of : "circle", "cross", "wave", "square" or "star"')
            user_guess = user_guess.lower()
            
    jupyprint(f'\nYou guessed **{user_guess}**.')
    jupyprint(f'\nThe actual card was **{current_card}**.')
   
    if user_guess == current_card:
        output = "CORRECT"
    else:
        output = "INCORRECT"
        
    jupyprint(f'\nYour guess was **{output}**.')
    
    return np.append(correct_guesses, output)