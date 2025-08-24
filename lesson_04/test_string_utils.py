import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
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


@pytest.mark.positive
@pytest.mark.parametrize("trim, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    (" тест", "тест"),
    (" 123", "123"),
    (" 04 апреля 2023", "04 апреля 2023")
])
def test_trim_positive(trim, expected):
    assert string_utils.trim(trim) == expected
    assert string_utils.trim("") == ""
    assert string_utils.trim("  hello  ") == "hello  "


@pytest.mark.parametrize("trim, expected", [
    ("1 23abc", "1 23abc"),
    ("", ""),
    (" ", "")
])
def test_trim_negative(trim, expected):
    assert string_utils.trim(trim) == expected
    assert string_utils.trim("") == ""


@pytest.mark.positive
@pytest.mark.parametrize()
def test_contains_positive():
    assert string_utils.contains("lesson", "a") == False
    assert string_utils.contains("lesson", "n") == True


@pytest.mark.positive
@pytest.mark.parametrize
def test_contains_negative():
    assert string_utils.contains("lesson", " ") == False


@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("lesson", "les", "son"),
    ("12345", "2", "1345"),
])
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("lesson", "les") == "son"


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("lesson", "les", "lesson"),
    ("12345", "2", "12345"),
])
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("lesson", "les") == "lesson"
    assert string_utils.delete_symbol("12345", "2") == "12345"
