from .data_handling import to_dict
from .data_handling import from_dict
from .data_handling import update_data
from main import game_closed

def Current_game_status():
       #This function will update the status of the game e.g.
       # Is Won, Is Lost, In Play
       return None

def is_won():
    # takes an input from game_status
    # store game status / history (to dict)
    # include a running total of how many games have been played
    # include a cumulative total of how many games have been won
    # display the "you have won" screen
    # offer an option to start a new game
    return {
          "message": "You won the game",
          "cumulative score": "",
          "No. of Games Won" : "",
          "message" : "Would you like to play again?"
           }

def is_lost():
    # similar to above in reverse
    return None

def is_closed(close_button_click,key,word_with_guessed_letters,data, json_filename ):
    #This is a function for if the game is exited:
    to_dict(key,word_with_guessed_letters,data, json_filename)
    return game_closed == True

def setup_new_guess(in_play_data):
     return None
#This will re-set the screen to allow the user to set
                        #up a new guess