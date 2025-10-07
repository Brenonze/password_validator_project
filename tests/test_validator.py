
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.validator import validate_password, ValidationResult


def test_valid_password():
    res = validate_password("GoodP@ssw0rd!")
    assert res.valid
    assert res.errors == []

@pytest.mark.parametrize("pw, expected_error", [
    ("short1A", "too_short"),
    ("alllowercase1!", "missing_uppercase"),
    ("ALLUPPERCASE1!", "missing_lowercase"),
    ("NoDigits!!", "missing_digit"),
    ("NoSpecial1A", "missing_special"),
    ("With Space1!", "contains_whitespace"),
    ("password", "common_password"),
])
def test_single_rule_violations(pw, expected_error):
    res = validate_password(pw)
    assert not res.valid
    assert expected_error in res.errors

def test_none_password():
    res = validate_password(None)
    assert not res.valid
    assert "password_missing" in res.errors

def test_non_string_password():
    res = validate_password(12345678)
    assert not res.valid
    assert "password_type_invalid" in res.errors

def test_multiple_errors():
    # too short, missing special, missing uppercase
    res = validate_password("abc1")
    assert not res.valid
    assert "too_short" in res.errors
    assert "missing_uppercase" in res.errors
    assert "missing_special" in res.errors

def test_custom_min_length():
    res = validate_password("Ab1!", min_length=4)
    assert res.valid
