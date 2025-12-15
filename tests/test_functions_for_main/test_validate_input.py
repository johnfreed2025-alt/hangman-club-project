import pytest
from hangman_code.functions_for_main.validate_input import Validate_input

def test_validate_input_accepts_lowercase():
    """Test to check that the function can work with a 
    lowercase letter"""
    test_letter = "a"
    used_letters = ""
    test_result = Validate_input(test_letter, used_letters = "")
    assert test_result is True

def test_validate_input_outputs_a_capital():
    """Test to check that the function can work with a 
    lowercase letter"""
    test_letter = "a"
    used_letters = ""
    expected = "A"
    test_result = Validate_input(test_letter, used_letters)
    assert test_result == expected


def test_validate_input_accepts_capital():
    """Test to check that the function can work with a 
    capital letter"""
    test_letter = "A"
    used_letters = ""
    test_result = Validate_input(test_letter, used_letters)
    assert test_result is True

def test_validate_input_rejects_multiple_characters():
    """Test to check that an error is returned if multiple characters
    are selected"""
    with pytest.raises(ValueError) as exc_info:
        test_letter = "AB"
        used_letters = ""
        Validate_input(test_letter, used_letters)
    assert "must be" in str(exc_info.value)
    
def test_validate_input_error_if_number_entered():
    """Test to check that the function returns an error 
    if a number is inserted"""
    with pytest.raises(ValueError) as exc_info:
                test_letter = "1"
                used_letters = ""
                Validate_input(test_letter, used_letters)
    assert "alphabetic" in str(exc_info.value)

def test_validate_input_if_special_character_entered():
    """Test to check that the function returns an error 
    if a special character is inserted"""
    with pytest.raises(ValueError) as exc_info:
                test_letter = "1"
                used_letters = ""
                Validate_input(test_letter, used_letters)
    assert "alphabetic" in str(exc_info.value)

def test_validate_input_cannot_repeat_previously_guessed_letter():
    """Test to check that the function returns an error 
    if an already guessed letter is provided again"""
    with pytest.raises(ValueError) as exc_info:
                used_letters = ["C"]
                test_letter = "C"
                Validate_input(test_letter, used_letters)
    assert "previously guessed" in str(exc_info.value)

