from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from nutrition_blog.web.models import Articles

UserModel = get_user_model()


class UserArticlesViews(TestCase):

    def test_get__two_articles__when_user_logged_in__expect_user_context_to_include_two_articles(self):
        articles_to_create = (
                Articles(
                        article_url_image = 'https://cfpen.org/wp-content/uploads/2019/05/Eat_Healthy_Blog_15May19.jpg',
                        article_tag_name = "Tips1",
                        article_title = "Article_title1",
                        description = "Description1",
                        user_id = 1,
                ),
                Articles(
                        article_url_image = 'https://cfpen.org/wp-content/uploads/2019/05/Eat_Healthy_Blog_15May19.jpg',
                        article_tag_name = "Tips2",
                        article_title = "Article_title2",
                        description = "Description2",
                        user_id = 1
                ),

        )

        Articles.objects.bulk_create(articles_to_create)

        user_data = {
                'email': 'myemail@mail.com',
                'password': 'testpassword123',
        }

        UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)
        response = self.client.get(reverse('user home page', kwargs = {
                'pk': 1,
        }
                                           ))

        articles = response.context_data["page_obj"].object_list

        self.assertEqual(len(articles), len(articles_to_create))

    def test_get__when_user_logged_in__return_status_code_302_and_redirect_to_User_Home_page_successfully(self):
        user_data = {
                'email': 'myemail@mail.com',
                'password': 'testpassword123',
        }

        UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)

        response = self.client.get(reverse('welcome page'))

        expected_url = reverse('user home page', kwargs = {'pk': 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url)

    def test_get__when_user_not_logged_in__return_status_code_200_and_redirect_to_Welcome_page_successfully(self):
        user_data = {
                'email': 'myemail@mail.com',
                'password': 'testpassword123',
        }

        UserModel.objects.create_user(**user_data)
        response = self.client.get(reverse('welcome page'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, '/')
        self.assertTemplateUsed(response, 'welcome_page.html')
