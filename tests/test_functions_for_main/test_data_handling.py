import pytest
from hangman_code.functions_for_main.data_handling import to_dict

def test_file_is_clear_for_test():

    open("persistence_for_test.json", "w").close()
    f = open("persistence_for_test.json", "r")
    assert f.read == ""


def test_to_dict_basic_structure():
    input = {"practice" : "Banana"}
    json_file = "persistence_for_test.json"
    expected = {'practice': 'Banana'}
    do = to_dict(input, json_file) 
    f = open("persistence_for_test.json")
    assert f.read == {'practice': 'Banana'} == expected


