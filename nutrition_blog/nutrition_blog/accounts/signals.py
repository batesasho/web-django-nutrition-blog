from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from nutrition_blog.accounts.models import Profile
from nutrition_blog.accounts.tasks import send_email_successful_registration, \
    user_profile_creation_after_user_registration
from nutrition_blog.secret_info import EMAIL_ADDRESS

UserModel = get_user_model()


@receiver(post_save, sender = UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        user_profile_creation_after_user_registration.delay(instance.id)

        # profile = Profile(
        #         user = instance,
        # )
        # profile.save()


@receiver(post_save, sender = UserModel)
def notify_user_after_registration(sender, instance, created, **kwargs):

    if created:
        send_email_successful_registration.delay(instance.pk)

        # if not using celery:
        # subject = "Account register confirmation"
        # from_email = EMAIL_ADDRESS
        # to_email = [instance.email]
        # message = "Welcome to Ivelina's blog." \
        #           "You have been successfully registered."
        #
        # try:
        #     send_mail(subject, message, from_email, to_email)
        # except ConnectionRefusedError:
        #     return HttpResponse('Sending email was rejected by the Mail server, please contact your administrator')
