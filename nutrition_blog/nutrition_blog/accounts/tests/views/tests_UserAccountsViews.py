from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from nutrition_blog.accounts.models import AppUser, Profile

UserModel = get_user_model()


class UserRegistrationViewTest(TestCase):

    VALID_USER_DATA = {
            'first_name': "MyFirstName",
            'email': 'myemail@mail.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
    }
    VALID_PROFILE_DATA = {
            'first_name': "MyFirstName",
    }

    def test_get__expect_correct_template_and_correct_status_code_returned(self):
        response = self.client.get(reverse('user register'))
        self.assertTemplateUsed(response, 'create_account_page.html')
        self.assertEqual(response.status_code, 200)

    def test_create_profile__when_all_valid__expect_to_succeed(self):
        self.client.post(
                reverse('user register'),
                data = self.VALID_USER_DATA,
        )

        user_profile = AppUser.objects.first()
        profile = Profile.objects.first()

        self.assertIsNotNone(user_profile)
        self.assertEqual(self.VALID_USER_DATA['email'], user_profile.email)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)


