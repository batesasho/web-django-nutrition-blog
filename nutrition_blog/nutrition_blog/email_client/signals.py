from django.dispatch import receiver
from nutrition_blog.email_client.tasks import consultation_contact_message_sending
from nutrition_blog.email_client.views import consultant_form_done


@receiver(consultant_form_done)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        consultation_contact_message_sending.delay(
                kwargs['subject'], kwargs['from_email'],
                kwargs['message'], kwargs['to_email'],

        )
