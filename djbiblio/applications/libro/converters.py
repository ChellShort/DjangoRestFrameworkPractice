from django.urls import register_converter
import re

def is_valid_regex(pattern: str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
    
def validate_string(pattern: str, text: str) -> bool:
    """
    Validates a string against a regex pattern.
    Returns True if the string matches the pattern, False otherwise.
    """
    if not is_valid_regex(pattern):
        return False
    
    return bool(re.fullmatch(pattern, text))


class ValidYearsConvert:
    regex = r'([2-9]\d{3,}|[3-9]\d{2}|199\d)'
    
    def to_python(self, value):
        validated = validate_string(self.regex, value)
        if validated and int(value) > 15:
            return value
        else:
            raise Exception("Error de año")
    
    def to_url(self, value):
        return value
    

class TwoDigitsNumber:
    regex = '[0-9]+'
    
    def to_python(self, value):            
        validated = validate_string(self.regex, value)
        if validated and int(value) > 15:
            return value
        else:
            raise Exception("Error de numero")
    
    def to_url(self, value):
        return value
    