from django.core import mail
from django.test import TestCase
from nutrition_blog.email_client.forms import ContactForm


class ContactFormTest(TestCase):
    valid_input_data = {
            'subject': "This is Subject",
            'message': 'This message wil be sent by ....',
    }

    def test_user_form__when_subject_and_message_are_valid__expect_form_validation_succeed(self):
        form = ContactForm(self.valid_input_data)
        self.assertTrue(form.is_valid())

    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'iv.healthy.blog@gmail.com', ['iv.healthy.blog@gmail.com'],
                       fail_silently = False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
