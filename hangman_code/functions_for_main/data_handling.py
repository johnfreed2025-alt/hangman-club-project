from json import load, dumps
from main import data
from hangman_code.functions_for_main.guessed_letters_and_words import used_letters_function
from hangman_code.functions_for_main.guessed_letters_and_words import guessed_words_function
from hangman_code.functions_for_main.scores_and_attempts_function import remaining_attempts_function
from hangman_code.functions_for_main.scores_and_attempts_function import remaining_attempts_function


def update_data(key, value, data):
        #This updates the dictionary each time a guess is made
        data.update({key: value})

def update_in_play_data(letter, 
                       guessed_word, 
                       attempts_remaining, 
                       current_score):

        """The updates to the game data shall now be created"""

        used_letters = used_letters_function(letter, used_letters)
        #This will update list of used letters

        words_guessed = guessed_words_function(guessed_word, words_guessed)
        #This will update the list of previously guessed words


        attempts_remaining = remaining_attempts_function(attempts_remaining)
        #This will update the number of remaining attempts

        current_score = update_score_function(current_score)
        #This will update the score value

def global_dictionary_update():

        # Update dictionary with updated guess_result
        update_data("word_progress", guess_result, data)
        # Update dictionary with used letters
        update_data("used_letters", letter, data)
        # Update dictionary with used word guesses
        update_data("guessed_words", guessed_word, data)
        # Update dictionary with game status
        update_data("game_status", current_game_status, data)
        # Update dictionary with remaining attempts
        update_data("remaining_attempts", attempts_remaining, data)
        # Update dictionary with score from last game
        update_data("score_keeping", current_score, data)
        # Update dictionary with cumulative score from last game
        update_data("cumulative score", cumulative_score, data)
        # Update dictionary with number of games played in total
        update_data("number_games_played", number_of_games_played, data)
        # Update dictionary with number of games won in total
        update_data("number_games_won", number_of_games_won, data)
        # Update dictionary with index of current game
        update_data("number_games_won", game_index, data)


def from_dict(key,json_filename):
        #if json_filename is None:
        #json_filename = config.json_filename
        #This function retrieves the game data from the storage area json
     
        with open(json_filename, 'r') as file: 
                data = load(file) # this is the dictionary
                value = data.get(key, None)  # returns None if key missing
                return value

def to_dict(data, json_filename):
        #This function inputs game data to the storage area json

                send_data = dumps(data, indent=4)
                with open(json_filename, "w") as f:
                        f.write(send_data)