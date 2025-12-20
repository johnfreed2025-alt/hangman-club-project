
#from word_selection import choose_word
#from game import Game
#from templates import Template

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# these functions are all in the functions_for_play_game folder

#-----------------------------------------------------------------------------
from enum import Enum
from hangman_code.game import Game
from hangman_code.functions_for_play_game.validate_input import Validate_input
from hangman_code.functions_for_play_game.make_guess import Make_guess
from hangman_code.functions_for_play_game.game_status_function import Current_game_status
from hangman_code.functions_for_play_game.start_game import Start_game
from hangman_code.functions_for_play_game.game_status_function import setup_new_guess
from hangman_code.functions_for_play_game.game_status_function import is_won
from hangman_code.functions_for_play_game.game_status_function import is_lost
from hangman_code.functions_for_play_game.game_status_function import is_closed
from hangman_code.functions_for_play_game.data_handling import update_in_play_data
from hangman_code.functions_for_play_game.start_game import Start_game_Selection
#-----------------------------------------------------------------------------
"""This is me showing off my kudos"""
#-----------------------------------------------------------------------------
#JUST WANTED TO HIGHLIGHT THIS IS NOT CHATGPT GENERATED. PURE ROANNE
#-----------------------------------------------------------------------------
"""The list of public parameters for playing :
These are needed as user inputs from app"""
#-----------------------------------------------------------------------------


letter = None

#-----------------------------------------------------------------------------
"""Below is the list of private parameters for running main"""
"""Else, the list of parameters for playing the Game is within Game.py"""
#-----------------------------------------------------------------------------

json_filename = "persistence.json"
game_closed = False
#-----------------------------------------------------------------------------
"""This is the constructor for the dictionary with various the 
inputs needed in functions_for_play_game.The initialised data itself is in 
game.py"""
#-----------------------------------------------------------------------------

# Now moved into data_handling so that all data and data handling are 
# kept together (Seperation of concerns)

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# I have moved these functions into the functions_for_play_game folder

#-----------------------------------------------------------------------------
"""This is the actual game logic / flow / main programme"""
#-----------------------------------------------------------------------------
def load_game(selection):
        current_game = Start_game_Selection(selection)
        return current_game

def play_game(current_game: dict, letter):
       
        game = Start_game(current_game, letter)
        # i.e. needs the letter from the user and the game object which is the
        #return from Start_game_selection

        while game["attempts_remaining"] > 0 & game_closed == False:

                try:
                       
                        Validate_input(letter, game["used_letters"])

                except (TypeError, ValueError):

                        return "Code needs to be written to reset / try again"

                else:
                        results = Make_guess(letter, game["word"], game["guess_result"])
                        game.guess_result = results.get("word_progress")
                        current_game_status = Current_game_status(results)
                        #This will update the status of the game e.g.
                                # Is Won, Is Lost, In Play

                        if current_game_status == 1: #"In Play via enum"

                                in_play_game = update_in_play_data(
                                        game.used_letters, 
                                        game.guessed_word, 
                                        game.attempts_remaining, 
                                        game.current_score)
                                
                                setup_new_guess(in_play_game)
                                #This will re-set the screen to allow the user 
                                # to set up a new guess

                        elif current_game_status == 2: # "Is Won" in Enum
                               is_won()
                               Start_game_Selection(load_game)
                                # if new game, return to play game
                                #this logic should go into the
                                #Start_game_selection function
                                      
                               
                        elif current_game_status == 3: #"Is Lost" in Enum
                                is_lost()
                                Start_game_Selection(load_game)
                                # if new game, return to play game
                                #this logic should go into the
                                #Start_game_selection function

                finally:
                       is_closed(load_game == None, json_filename, game)
                       #Logic to be worked out
         #The dictionary will now be updated - ready to store in persistence
         # if we wanted to resume the game later"""
                       return game_closed == True
