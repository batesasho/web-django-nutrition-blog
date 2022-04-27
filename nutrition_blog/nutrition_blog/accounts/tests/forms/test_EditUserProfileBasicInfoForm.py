from django.test import TestCase

from nutrition_blog.accounts.forms.user_form import EditUserProfileBasicInfoForm


class EditUserProfileFormTest(TestCase):
    valid_input_data = {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'age': 23,
            'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
            'gender': "Male",

    }

    def test_user_form__when_input_data_is_valid__expect_form_validation_succeed(self):
        form = EditUserProfileBasicInfoForm(self.valid_input_data)
        self.assertTrue(form.is_valid())

    def test_user_form__when_first_name_is_invalid_contains_digits__expect_form_validation_failure(self):
        invalid_first_name = {
                'first_name': '123FirstName',
                'last_name': 'NewLastName',
                'age': 23,
                'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
                'gender': "Male",

        }
        form = EditUserProfileBasicInfoForm(invalid_first_name)
        self.assertFalse(form.is_valid())

    def test_user_form__when_last_name_is_invalid_contains_digits__expect_form_validation_failure(self):
        invalid_last_name = {
                'first_name': 'FirstName',
                'last_name': '123321LastName',
                'age': 23,
                'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
                'gender': "Male",

        }
        form = EditUserProfileBasicInfoForm(invalid_last_name)
        self.assertFalse(form.is_valid())

    def test_user_form__when_age_is_invalid_contains_negative_value__expect_form_validation_failure(self):
        invalid_age = {
                'first_name': 'FirstName',
                'last_name': 'LastName',
                'age': -23,
                'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
                'gender': "Male",

        }
        form = EditUserProfileBasicInfoForm(invalid_age)
        self.assertFalse(form.is_valid())

    def test_user_form__when_gender_is_invalid__expect_form_validation_failure(self):
        invalid_gender = {
                'first_name': 'FirstName',
                'last_name': 'LastName',
                'age': 23,
                'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
                'gender': "NoGenderField",

        }
        form = EditUserProfileBasicInfoForm(invalid_gender)
        self.assertFalse(form.is_valid())