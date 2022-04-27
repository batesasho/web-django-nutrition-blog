from django.test import TestCase

from nutrition_blog.accounts.models import AppUser


class UserAppTest(TestCase):

    def test_create_user__when_email_is_correct__expect_user_created(self):
        user = AppUser(email = 'testemail@test.com')
        user.save()
        self.assertEqual('testemail@test.com', user.email)
        self.assertIsNotNone(user.id)
