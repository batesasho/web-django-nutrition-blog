from celery import shared_task
from django.core.mail import send_mail
from django.http import HttpResponse

from nutrition_blog.accounts.models import Profile, AppUser
from nutrition_blog.secret_info import EMAIL_ADDRESS


@shared_task
def send_email_successful_registration(instance_pk):
    email = AppUser.objects.\
        get(pk = instance_pk).email
    first_name = Profile.objects\
        .get(pk = instance_pk).first_name

    subject = "Account register confirmation"
    from_email = EMAIL_ADDRESS
    to_email = [email]
    message = f"{first_name.capitalize()}, welcome to Ivelina's Nutrition blog." \
              "\nYou have been successfully registered."

    try:
        send_mail(subject, message, from_email, to_email)
    except ConnectionRefusedError:
        return HttpResponse('Sending email was rejected by the Mail server, please contact your administrator')


@shared_task
def user_profile_creation_after_user_registration(user_pk):
    profile = Profile(
            user = user_pk,
    )
    profile.save()
