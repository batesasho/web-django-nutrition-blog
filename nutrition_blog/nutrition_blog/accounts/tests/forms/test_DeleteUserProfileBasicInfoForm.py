from django.test import TestCase

from nutrition_blog.accounts.forms.user_form import DeleteUserProfileBasicInfoForm


class DeleteUserProfileFormTest(TestCase):
    valid_input_data = {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'age': 23,
            'profile_image': "profile_photo/Whatsapp-DP-Profile-Images-72.jpg",
            'gender': "Male",

    }

    def test_user_form__when_input_data_is_valid__expect_form_validation_succeed(self):
        form = DeleteUserProfileBasicInfoForm(self.valid_input_data)
        self.assertTrue(form.is_valid())

    def test_user_form__when_input_data_is_valid__expect_user_deleted(self):
        form = DeleteUserProfileBasicInfoForm(self.valid_input_data)
        form.instance.pk = 1
        self.assertTrue(form.is_valid())
        form.save()
        self.assertIsNone(form.instance.pk)
