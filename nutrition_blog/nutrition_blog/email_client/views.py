from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import generic as views
from django.urls import reverse_lazy

from .forms import ContactForm

UserModel = get_user_model()


# def contact_view(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = request.user.email
#             message = form.cleaned_data['message']
#             to_email = ['iv.healthy.blog@gmail.com']
#
#             try:
#                 message += f'\n\nThis message was sent by {from_email}'
#                 send_mail(subject, message, from_email, to_email)
#             except BadHeaderError:  # security check reasons
#                 return HttpResponse('Invalid header found.')
#
#             return redirect('success')
#
#     return render(request, "consultant_page.html", {'form': form})


class ConsultantView(auth_mixin.LoginRequiredMixin, views.FormView):
    template_name = "consultant_page.html"
    success_url = reverse_lazy('success')
    form_class = ContactForm

    def form_valid(self, form):
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = self.request.user.email
            message = form.cleaned_data['message']
            to_email = ['iv.healthy.blog@gmail.com']

            try:
                message += f'\n\nThis message was sent by {from_email}'
                send_mail(subject, message, from_email, to_email)
            except BadHeaderError:  # security check reasons
                return HttpResponse('Invalid header found.')

        return super().form_valid(form)


class SuccessEmailSentView(auth_mixin.LoginRequiredMixin, views.TemplateView):
    template_name = 'success_email_send.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.request.user.profile.first_name
        context['user_name'] = user_name
        return context

