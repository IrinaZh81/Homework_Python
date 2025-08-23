import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])

def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    assert string_utils.capitalize("") == "" 

def test_trim_positive():
    assert string_utils.trim
    assert string_utils.trim("") == ""
    assert string_utils.trim("  hello  ") == "hello  "

def test_trim_negative():
    assert string_utils.trim("") == ""

def test_contains_positive():
    assert string_utils.contains("lesson", "a") == False
    assert string_utils.contains("lesson", "n") == True

def test_contains_negative():
    assert string_utils.contains("lesson", " ") == False

def test_delete_symbol_positive():
    assert string_utils.delete_symbol("lesson", "les") == "son"

def test_delete_symbol_negative():
    assert string_utils.delete_symbol("lesson", "les") == "lesson"
    assert string_utils.delete_symbol("", "123") == "123"




