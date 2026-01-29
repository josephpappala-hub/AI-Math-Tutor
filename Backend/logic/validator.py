# validator.py
# Core logic for Class 9 Number Systems

from fractions import Fraction
import math
import re

# Check if a number is rational
def is_rational(value):
    try:
        # Convert float to fraction and check if exact
        Fraction(value)
        return True
    except:
        return False

# Check if an answer for exponent simplification is correct
def check_exponent_answer(correct, student):
    try:
        # Convert to float and compare
        return float(correct) == float(student)
    except:
        return False

# General function to check number type
def check_number_type(value, expected_type):
    if expected_type.lower() == "rational":
        return is_rational(value)
    elif expected_type.lower() == "irrational":
        return not is_rational(value)
    else:
        return False

def validate_polynomial(answer: str) -> bool:
    """Validate if answer is a valid polynomial."""
    # Simple polynomial pattern: ax^n + bx^m + ...
    pattern = r'^[+-]?\d*x?\^?\d*([+-]\d*x?\^?\d*)*$'
    return bool(re.match(pattern, answer.replace(" ", "")))

def validate_integer(answer: str) -> bool:
    """Validate if answer is a valid integer."""
    try:
        int(answer.strip())
        return True
    except ValueError:
        return False

def validate_answer_type(answer: str, expected_type: str) -> bool:
    """Validate answer based on expected type."""
    if expected_type == "integer":
        return validate_integer(answer)
    elif expected_type == "polynomial":
        return validate_polynomial(answer)
    else:
        return True  # Default: any answer is valid
