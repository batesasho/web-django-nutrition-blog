from django.test import TestCase

from nutrition_blog.accounts.forms.user_form import UserRegistrationForm



class RegistrationFormTest(TestCase):
    valid_input_data = {
            'first_name': "FirstName",
            'email': 'TestEmail@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword1',
    }

    invalid_input_data = {
            'first_name': "FirstName123isInvalid",
            'email': 'TestEmail@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword1',
    }

    def test_user_form__when_input_data_is_valid__expect_form_validation_succeed(self):
        form = UserRegistrationForm(self.valid_input_data)
        self.assertTrue(form.is_valid())

    def test_user_form__when_first_name_is_incorrect__expect_form_validation_failure(self):
        form = UserRegistrationForm(self.invalid_input_data)
        self.assertFalse(form.is_valid())
