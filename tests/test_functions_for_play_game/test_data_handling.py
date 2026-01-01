import pytest
import json
from hangman_code.functions_for_play_game.data_handling import to_dict
from hangman_code.functions_for_play_game.data_handling import from_dict
from hangman_code.game import Game


@pytest.fixture
def from_dict_expected_keys_and_values():
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
    return expected


def test_to_dict_raises_error_if_directory_missing():
    location = "missing_dir/file.json"
    data = {"message": ""}

    with pytest.raises(FileNotFoundError):
        to_dict(data, location)

def test_to_dict_fails_when_file_unwritable(tmp_path):
    file_path = tmp_path / "test.json"
    file_path.touch()
    file_path.chmod(0o400)  # read-only

    with pytest.raises(PermissionError):
        to_dict({"message": "hello"}, file_path)

def test_to_dict_basic_functionality(tmp_path):
#Test that the json file is written to as expected
    file_path = tmp_path / "test.json"
    input_data = {"message": "Banana"}
    to_dict(input_data, file_path)
    with open(file_path) as f:
        data = json.load(f)
    assert data == input_data

def test_to_dict_returns_None(tmp_path):
    file_path = tmp_path / "test.json"
    input_data = {"message": "Banana"}
    result = to_dict(input_data, file_path)
    assert result == None

def test_to_dict_returns_error_if_no_data(tmp_path):
    file_path = tmp_path / "test.json"
    input_data = {}
    with pytest.raises(ValueError):
        to_dict(input_data, file_path)

def test_to_dict_accepts_integers_as_values(tmp_path):
#Test that the json file accepts integers as values
    file_path = tmp_path / "test.json"
    input_data = {"attempts_remaining": 100}
    to_dict(input_data, file_path)
    with open(file_path) as f:
        data = json.load(f)
    assert data == input_data

def test_to_dict_accepts_lists(tmp_path):
    file_path = tmp_path / "test.json"
    data = [("message", "26"), ("attempts_remaining", 5)]
    to_dict(data, file_path)
    with open(file_path) as f:
        saved = json.load(f)
    assert saved["message"] == "26"

def test_only_valid_key_value_pairs_can_be_supplied_to_to_dict(tmp_path):
    #Test that only key, value pairs can be sent to dict
    file_path = tmp_path / "test.json"
    data = {"game_name": 30}
    with pytest.raises(TypeError):
        to_dict(data, file_path)

def test_to_dict_rejects_empty_keys_to_maintain_code_clarity(tmp_path):
    file_path = tmp_path / "test.json"
    data = {"": "item 1"}
    with pytest.raises(KeyError):
        to_dict(data, file_path)

def test_to_dict_only_allows_legitimate_keys(tmp_path):
# Only keys allowed as described in Game.py
    file_path = tmp_path / "test.json"
    data = {"Not allowed": "Value"}
    with pytest.raises(KeyError):
        to_dict(data, file_path)

def test_to_dict_only_allows_legitimate_value_types_according_to_key(tmp_path):
# In this test, word value should be a list
    file_path = tmp_path / "test.json"
    data = {"word": 1}
    with pytest.raises(ValueError):
        to_dict(data, file_path)


def test_to_dict_rejects_repeated_keys_in_same_data_dump(tmp_path):
    file_path = tmp_path / "test.json"
    data = [("word", ("d","o","g")), ("word", ("c","a","t"))]
    with pytest.raises(KeyError):
        to_dict(data, file_path)

def test_to_dict_keys_require_exact_match(tmp_path):
    file_path = tmp_path / "test.json"
    data = {"message": "", "attempts_remaining": "", "word" : ""}
    to_dict(data, file_path)
    update_data = {"Message": "", "attempts_remaining": "", "word" : ""}
    with pytest.raises(KeyError):
        to_dict(update_data, file_path)

def test_to_dict_allows_overwrites(tmp_path):
    file_path = tmp_path / "test.json"
    data = [("message", "hello"), ("message", "Bye Bye")]
    to_dict(data, file_path)
    with open(file_path) as f:
        saved = json.load(f)
    assert saved["message"] == "Bye Bye"


def test_to_dict_persists_values_which_are_not_overwritten(tmp_path):
    data = {"message": "hello", "attempts_remaining": 2, "word" : "a"}
    file_path = tmp_path / "test.json"
    persist = to_dict(data, file_path)
    update_data = {"attempts_remaining": 100, "word" : "z"}
    with open(file_path) as f:
        saved = json.load(f)
    assert saved["message"] == "hello"

def test_only_valid_syntax_can_be_sent_to_persistence(tmp_path):
    #Test that only none nested python dictionary or list can be sent.
    file_path = tmp_path / "test.json"
    data = {
    "Parameters": {
        "game_name": 30,
        "message": "hello"
    }
}

    with pytest.raises(TypeError):
        to_dict(data, file_path)

def test_check_json_file_is_found_for_from_dict():
#Setup test that the expected test json file is present
    result = 1
    try:
        f = open("persistence.json")
    except ValueError as err:
        result = 2
    assert result == 1
    f.close()

def test_from_dict_basic_functionality(from_dict_expected_keys_and_values):
#Test that data is returned from the persistence file and is correct

    json_file = "tests/persistence_for_test2.json"
    result = from_dict(json_file)
    expected = from_dict_expected_keys_and_values
    assert result == expected
    json_file.close()

def test_from_dict_returns_error_if_value_is_wrong_format():
# Number of games won has been changes to "three" -> str rather than 3 -> int
    json_file = "tests/persistence_for_test3.json"
    with pytest.raises(TypeError):
        from_dict(json_file)

def test_from_dict_returns_error_if_keys_are_missing():
# Number of games won has been deleted
    json_file = "tests/persistence_for_test4.json"
    with pytest.raises(KeyError):
        from_dict(json_file)

def test_from_dict_raises_error_for_empty_file(tmp_path):
    file_path = tmp_path / "test.json"
    file_path.touch()  # create empty file

    with pytest.raises(ValueError):
        from_dict(file_path)


def test_to_dict_from_dict_round_trip(tmp_path, from_dict_expected_keys_and_values):
    file = tmp_path / "game.json"
    data = from_dict_expected_keys_and_values
    to_dict(data, file)
    result = from_dict(file)
    assert result == data


