from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure the Name contains only letters.')


@deconstructible
class ValidateMaxSizeMB:
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        self.max_size_mb = 5 * 1024 * 1024
        filesize = value.file.size
        if filesize > self.max_size_mb:
            raise ValidationError(f"Max image size is {self.max_size_mb:.2f} MB")
