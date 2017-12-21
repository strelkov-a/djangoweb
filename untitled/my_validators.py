from django.core.exceptions import ValidationError


class NameAndSlugValidator(object):

    def __call__(self, value):
        message = "This field cannot be longer than 200 symbols."
        code = 'Invalid'
        if len(value) > 200:
            raise ValidationError(message, code)


class InterfaceCapacityValidator(object):

    def __call__(self, value):
        message = "This field cannot be longer than 30 symbols."
        code = 'Invalid'
        if len(value) > 30:
            raise ValidationError(message, code)