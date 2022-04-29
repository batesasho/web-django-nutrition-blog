from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from nutrition_blog.accounts.forms.user_form import UserPasswordResetForm
from nutrition_blog.accounts.models import AppUser, Profile

UserModel = get_user_model()


class ResetUserProfileFormTest(TestCase):

    VALID_USER_DATA = {
            'first_name': "MyFirstName",
            'email': 'myemail@mail.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
    }

    def test_user_form__when_email_is_registered_in_DB__expect_form_validation_succeeded(self):

        self.client.post(
                reverse('user register'),
                data = self.VALID_USER_DATA,
        )

        data = {
                'email': self.VALID_USER_DATA['email'],
        }

        form = UserPasswordResetForm(data)
        self.assertTrue(form.is_valid())

    def test_user_form__when_email_is_not_registered_in_DB__expect_form_validation_failure(self):
        self.client.post(
                reverse('user register'),
                data = self.VALID_USER_DATA,
        )

        data = {
                'email': "incorrect@email.address.com",
        }

        form = UserPasswordResetForm(data)
        expected_result = 'There is no user registered with the specified e-mail address, ' \
                          'please enter a registered email.'
        self.assertFalse(form.is_valid())
        self.assertEqual(expected_result, form.errors['email'][0])
