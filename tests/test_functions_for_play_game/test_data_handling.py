import pytest
import json
from hangman_code.functions_for_play_game.data_handling import to_dict
from hangman_code.functions_for_play_game.data_handling import from_dict

def test_check_json_file_is_found_for_to_dict_tests():
#Test that the expected test json file is present
    try:
        json.loads("persistence_for_test.json")
    except ValueError as err:
        result = 2
    result = 1
    assert result == 1
    ("persistence_for_test.json").close()

def test_check_json_file_is_found_for_from_dict_tests():
#Test that the expected test json file is present
    try:
        json.loads("persistence_for_test2.json")
    except ValueError as err:
        result = 2
    result = 1
    assert result == 1
    ("persistence_for_test2.json").close()

def test_file_is_clear_for_test():
#Test that this file clearing method will work for the following tests to run
    open("persistence_for_test.json", "w").close()

def test_game_and_data_handling_use_same_keys():
    assert 1 == 2

def test_valid_data_format_supplied_to_to_dict():
    assert 1 == 2

def test_to_dict_basic_functionality():
#Test that the json file is written to
    input_data = {"practice": "Banana"}
    json_file = "persistence_for_test.json"

    to_dict(input_data, json_file)

    with open(json_file) as f:
        data = json.load(f)
    assert data == input_data
    open("persistence_for_test.json", "w").close()

def test_to_dict_closes_file_after_use():
    assert 1 == 2

def test_from_dict_basic_functionality():
#Test that data is returned from the persistence file and is correct

    json_file = "persistence_for_test2.json"
    result = from_dict(json_file)
    expected = {
        "game_name": "Ronald",
        "word": ["D", "O", "G"],
        "game_id": 42,
        "current_score": 52,
        "template": "Resume",
        "message": "The only way is up",
        "used_letters": ["A", "B", "C"],
        "game_started": True,
        "current_game_status": 1,
        "accepted_letters": ["O", "G"],
        "guess_result": ["_", "O", "G"],
        "attempts_remaining": 2,
        "guessed_word": ["BOG"],
        "words_guessed": ["BOG", "FOG"],
        "Start_Game_Selection": 2,
        "game_closed": False,
        "cumulative_score": 1010101012,
        "number_of_games_played": 100,
        "number_of_games_won": 3,
              }
    assert result == expected
    ("persistence_for_test2.json").close()

def test_from_dict_closes_file_after_use():
    assert 1 == 2

def test_from_dict_comntains_required_data_keys():
    assert 1 == 2

def test_from_dict_contains_required_data_format():
    assert 1 == 2
