from django.core.exceptions import ValidationError


class name_and_slug_validator(object):

    def __call_():
        message = "This field cannot be longer than 200 symbols."
        code = 'Invalid'
        if len(value) > 200:
            raise ValidationError(message, code)
