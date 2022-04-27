from unittest import TestCase

from django.core.exceptions import ValidationError

from nutrition_blog.accounts.validators import validate_only_letters


class ValidateOnlyLetters(TestCase):
    VALID_INPUT = 'ThisIsValidInput'
    INVALID_INPUT_DIGITS = 'ThisIs_InValidInput123'
    INVALID_INPUT_DOLLAR_SIGN = 'ThisIs$InValidInput'

    def test__contains_letters_only__expected_succeed(self):
        result = validate_only_letters(self.VALID_INPUT)
        self.assertIsNone(result)

    def test__contains_letters_and_digits__raise_ValidationError(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_letters(self.INVALID_INPUT_DIGITS)

        expected_message = 'Ensure the Name contains only letters.'
        received_message = context.exception.args[0]
        self.assertEqual(expected_message, received_message)

    def test__contains_letters_and_dollar_sign__raise_ValidationError(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_letters(self.INVALID_INPUT_DOLLAR_SIGN)

        expected_message = 'Ensure the Name contains only letters.'
        received_message = context.exception.args[0]
        self.assertEqual(expected_message, received_message)
