# main program
#from word_selection import choose_word
#from game import Game
#from templates import Template

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# these functions are all in the functions_for_main folder

#-----------------------------------------------------------------------------

from hangman_code.functions_for_main.validate_input import Validate_input
from hangman_code.functions_for_main.make_guess import Make_guess
from hangman_code.functions_for_main.game_status_function import Current_game_status
from hangman_code.functions_for_main.start_game import Start_game
from hangman_code.functions_for_main.game_status_function import setup_new_guess
from hangman_code.functions_for_main.game_status_function import is_won
from hangman_code.functions_for_main.game_status_function import is_lost
from hangman_code.functions_for_main.game_status_function import is_closed
from hangman_code.functions_for_main.data_handling import update_in_play_data
from hangman_code.functions_for_main.start_game import Start_game_Selection
from hangman_code.functions_for_main.data_handling import global_dictionary_update
#-----------------------------------------------------------------------------
"""This is me showing off my kudos"""
#-----------------------------------------------------------------------------
#JUST WANTED TO HIGHLIGHT THIS IS NOT CHATGPT GENERATED. PURE ROANNE
#-----------------------------------------------------------------------------
"""This is the list of Configuration Variables and inputs for playing 
the Game"""
#-----------------------------------------------------------------------------
key = ""
guess_result = ["_","B","_","_","_","_"]
letter = "" #input from the user
json_filename = "persistence.json" #location of the data store
used_letters = ["_"]
attempts_remaining = 10
current_game_status = "Not Started"
guessed_word = [""]
words_guessed = [""]
current_score = 0
word = "" # will get word from word_selection
Start_Game_Selection = "" # will be click on New, Resume or Exit from the user,
game_index = ""
game_closed = False
cumulative_score = 0
number_of_games_played = 0
number_of_games_won = 0
#-----------------------------------------------------------------------------
"""This is the constructor for the dictionary for the game data. It contains
lots of useful inputs to be supplied by the user from app.py or
from word_selection"""
#-----------------------------------------------------------------------------
data = {"word_progress": guess_result, 
        "used_letter": used_letters,
        "guessed_words": guessed_word,
        "game_status" : current_game_status,
        "remaining_attempts" : attempts_remaining,
        "score_keeping" : current_score,
        "cumulative_score" : cumulative_score,
        "number_games_played" : number_of_games_played,
        "number_games_won" : number_of_games_won,
        "current_game_index" : game_index,
        }

#-----------------------------------------------------------------------------
"""These are the functions used in the main programme"""
#-----------------------------------------------------------------------------

# I have moved these functions into the functions_for_main folder

#-----------------------------------------------------------------------------
"""This is the actual game logic / flow / main programme"""
#-----------------------------------------------------------------------------
def play_game(Start_Game_Selection):
       
        Start_game(letter, word, guess_result)

        while attempts_remaining > 0 & game_closed == False:

                try:
                       
                        Validate_input(letter, used_letters)

                except (TypeError, ValueError):

                        return "Code needs to be written to reset / try again"

                else:
                        results = Make_guess(letter, word, guess_result)
                        guess_result = results.get("word_progress")
                        current_game_status = Current_game_status()
                        #This will update the status of the game e.g.
                                # Is Won, Is Lost, In Play

                        if current_game_status == "In Play":

                                in_play_data = update_in_play_data(
                                        used_letters, 
                                        guessed_word, 
                                        attempts_remaining, 
                                        current_score)
                                
                                new_guess_setup = setup_new_guess(in_play_data)
                                #This will re-set the screen to allow the user 
                                # to set up a new guess

                        elif current_game_status == "Is Won":
                               is_won()
                               Start_game_Selection()
                                # if new game, return to play game
                                #missing some logic here
                                      
                               
                        elif current_game_status == "Is Lost":
                                is_lost()
                                Start_game_Selection()
                                # if new game, return to play game
                                #missing some logic here

                finally:
                       
                       #Logic to be worked out
                       return None

 

        is_closed()


        """The dictionary will now be updated - ready to store in persistence
          if we wanted to resume the game later"""

        global_dictionary_update(
                letter,
                guessed_word,
                current_game_status,
                attempts_remaining,
                current_score,
                cumulative_score,
                number_of_games_played,
                number_of_games_won,
                game_index,
                )


# These 3 functions below are what chatGPT suggested to do with 
# the flask app. I think they are needed to configure the new game

def admin ():
    return None

def send_registration():
    return None









