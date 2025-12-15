from hangman_code.functions_for_main.other_game_data import index

def new_game ():
    
    game_index = index()
    #word = choose_word()
    # This shall call on the word_selection class to get a word
    #  and pass this into the game Class constructor
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # The get_render function in templates will need to be called
    return None

# or 

def resume_game ():
    return None
    # This shall call on the from_dict function and pass data from 
    # persistance into the Game Class as the arguments
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # It should flash up an error message to the user if there 
    # is no game to resume