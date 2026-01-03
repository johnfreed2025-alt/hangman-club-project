import pytest
from hangman_code.functions_for_play_game.start_game import new_game
from hangman_code.functions_for_play_game.start_game import resume_game


def test_new_game ():

    #word = choose_word()
    # This shall call on the word_selection class to get a word
    #  and pass this into the game Class constructor
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # The get_render function in templates will need to be called
    assert 1 == 2


def test_resume_game ():
    # This shall call on the from_dict function and pass data from 
    # persistance into the Game Class as the arguments
    # The output shall be returned to the user as an HTTP/HTTPS 
    # format via the convertor send_request function
    # It should flash up an error message to the user if there 
    # is no game to resume
    assert 1 == 2