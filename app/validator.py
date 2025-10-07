import re
from typing import List, NamedTuple

COMMON_PASSWORDS = {
    "password", "12345678", "123456", "qwerty", "abc123", "letmein", "admin", "welcome"
}

class ValidationResult(NamedTuple):
    valid: bool
    errors: List[str]

def validate_password(pw: str, min_length: int = 8) -> ValidationResult:
    errors = []
    if pw is None:
        errors.append("password_missing")
        return ValidationResult(False, errors)
    if not isinstance(pw, str):
        errors.append("password_type_invalid")
        return ValidationResult(False, errors)
    if len(pw) < min_length:
        errors.append("too_short")
    if any(c.isspace() for c in pw):
        errors.append("contains_whitespace")
    if not re.search(r'[A-Z]', pw):
        errors.append("missing_uppercase")
    if not re.search(r'[a-z]', pw):
        errors.append("missing_lowercase")
    if not re.search(r'\d', pw):
        errors.append("missing_digit")
    # special character: any non-alphanumeric
    if not re.search(r'[^A-Za-z0-9]', pw):
        errors.append("missing_special")
    if pw.lower() in COMMON_PASSWORDS:
        errors.append("common_password")
    return ValidationResult(len(errors) == 0, errors)
