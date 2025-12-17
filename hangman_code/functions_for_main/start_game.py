def Start_game_Selection (load_game):
    #User can select either start a new game, resume game, exit game
    # or factory reset. The input to this function is an enum
#class load_game(Enum): 
        #NEW_GAME = 0
        #RESUME_GAME = 1
        #EXIT_GAME = 2
        #FACTORY_RESET = 3

  # if new game, return to play game in main                
  # #this logic should go into this function


    # To create all of these functions:

    # Write a test in test_start_game_selection - check it fails (Click 
    # on the scientific jar logo on the menu on the left to run the test)
    # This test should be for the most the most basic first step of the 
    #function
    # Then write the function code to pass the test. Check the test passes: 
    # Then write the next test the function has to pass - check the test fails
    # Then write the function code to pass the test
    # So on and so forth
    return None


def Start_game(letter):
    return None


def new_game ():
    
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
    # It will need to select the 'new game' template
    # You will need to get hold of all of the other persistence data (such
    # as cumululative score etc) via data_handling

    return None

# or 

def resume_game ():
    
    # Consider that this enum class exists in game.py in the function design

     #class Game_status(Enum): 
        #NEW_GAME = 0
        #IN_PLAY = 1
        #WON = 2
        #LOST = 3
    return None
    # This shall call on the from_dict function in data_handling 
    # and pass data from persistance into the Game Class as the arguments
