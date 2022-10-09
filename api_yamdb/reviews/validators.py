from django.core.exceptions import ValidationError
import re

def validate_username(value):
    if value == 'me':
        raise ValidationError(
            "Username 'me' is not valid",
            params={'value':value}
        )
        
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            (f'Не допустимые символы <{value}> в нике.'),
            params={'value': value},
        )