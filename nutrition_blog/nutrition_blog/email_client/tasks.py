from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


@shared_task
def consultation_contact_message_sending(*args):
    subject, from_email, message, to_email = args
    try:
        send_mail(subject = subject, message = message, from_email = from_email, recipient_list = to_email)
    except BadHeaderError:  # security check reasons -> avoid header injection
        return HttpResponse('Invalid header found.')
