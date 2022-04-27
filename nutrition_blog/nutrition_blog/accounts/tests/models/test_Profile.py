from django.core.exceptions import ValidationError
from django.test import TestCase
from nutrition_blog.accounts.models import Profile, AppUser


class ProfileTest(TestCase):

    VALID_USER_DATA = {
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            "age": 10,
            'gender': 'Male',

    }

    def setUp(self):
        self.user = AppUser.objects.create(email = 'testemail@test.com', password = 'testemail123')

    def test_create_user_profile__when_input_is_correct__expect_profile_created(self):
        user_created = self.user
        user_profile = Profile(**self.VALID_USER_DATA, user = user_created)
        user_profile.save()
        self.assertEqual(self.VALID_USER_DATA['first_name'], user_profile.first_name)
        self.assertEqual(self.VALID_USER_DATA['last_name'], user_profile.last_name)
        self.assertEqual(self.VALID_USER_DATA['age'], user_profile.age)
        self.assertEqual(self.VALID_USER_DATA['gender'], user_profile.gender)
        self.assertIsNotNone(user_profile.pk)

    def test_create_user_profile__when_first_name_contains_digit__expect_profile_ValidationError(self):
        self.VALID_USER_DATA['first_name'] = "Firstnamecontain5"

        user_profile = Profile(**self.VALID_USER_DATA, user = self.user)
        with self.assertRaises(ValidationError) as context:
            user_profile.full_clean()
            user_profile.save()
        self.assertIsNotNone(context.exception)

    def test_create_user_profile__when_first_name_contains_special_signs__expect_profile_ValidationError(self):
        self.VALID_USER_DATA['first_name'] = "Firstnameco$_ntain"

        user_profile = Profile(**self.VALID_USER_DATA, user = self.user)
        with self.assertRaises(ValidationError) as context:
            user_profile.full_clean()
            user_profile.save()
        self.assertIsNotNone(context.exception)

    def test_create_user_profile__when_image_size_is_greater_than_5MB__expect_ValidationError(self):
        profile_image = 'bigger_than_5MB_picture.jpg'
        user_profile = Profile(**self.VALID_USER_DATA, profile_image = profile_image, user = self.user)
        with self.assertRaises(ValidationError) as context:
            user_profile.full_clean()
            user_profile.save()
        self.assertIsNotNone(context.exception)

    def test_create_user_profile__when_image_size_is_less_than_5MB__expect_profile_created(self):
        profile_image = 'default.jpg'
        user_profile = Profile(**self.VALID_USER_DATA, profile_image = profile_image, user = self.user)
        self.assertIsNotNone(user_profile.pk)
