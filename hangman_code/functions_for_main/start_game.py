from hangman_code.game import Game
from hangman_code.functions_for_main.data_handling import from_dict
from hangman_code.word_selection import choose_word

def Start_game_Selection (load_game):
    #User can select either start a new game, resume game, exit game
    # or factory reset. The input to this function is an enum
#class load_game(Enum): 
        #NEW_GAME = 0
        #RESUME_GAME = 1
        #EXIT_GAME = 2
        #FACTORY_RESET = 3

  # there will be some sort of 'if' selection: e.g. a NEW_GAME will call the
  #new_game function


    # To create all of these functions:

    # Write a test in test_start_game_selection - check it fails (Click 
    # on the scientific jar logo on the menu on the left to run the test)
    # This test should be for the most the most basic first step of the 
    #function
    # Then write the function code to pass the test. Check the test passes: 
    # Then write the next test the function has to pass - check the test fails
    # Then write the function code to pass the test
    # So on and so forth
    game_object = game_object = 0 # placeholder until game_object is 
    #initialised properly
    return game_object


def new_game (Game_status):
    # get word from word selection
    # get game object and data from data_handling.initialise_game_and_data
    # Consider that this enum class exists in game.py in the function design

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3
    
    #word = choose_word()
    # This shall call on the word_selection class to get a word
    #  and pass this into the game Class constructor via the update_data 
    # function in data_handling.
    # You will need to make a new object of game
    # It will need to select the 'new game' template
    # You will need to get hold of all of the other persistence data (such
    # as cumululative score etc) via data_handling
    game_object = 0 # placeholder until game_object is initialised properly
    return game_object

# or 

def resume_game (Game_status):
    
    # Consider that this enum class exists in game.py in the function design
     # You will need to create a object from Game
     # use data from from_dict for this

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3

        # Return the game object
    game_object = 0 # placeholder until game_object is initialised properly
    return game_object

def Start_game(letter, game_object):

    #This loads the screen using the data from either new game or resume game
    # The user can now enter the first letter
    return None

    # This shall call on the from_dict function in data_handling 
    # and pass data from persistance into the Game Class as the arguments
