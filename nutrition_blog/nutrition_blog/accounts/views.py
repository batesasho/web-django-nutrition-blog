from django.contrib import messages
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from nutrition_blog.accounts.forms.user_form import UserRegistrationForm, DeleteUserProfileBasicInfoForm, \
    EditUserProfileBasicInfoForm
from nutrition_blog.accounts.models import Profile

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'create_account_page.html'

    # success_url = reverse_lazy('user home page')

    # auto login when user register
    def form_valid(self, form):
        user_valid = super().form_valid(form)
        login(self.request, self.object)
        return user_valid

    def get_success_url(self):
        return reverse_lazy('consultant')
        # return reverse('user home page',
        #                kwargs = {
        #                        'pk': self.object.id,
        #                }
        #                )


class UserLoginView(auth_views.LoginView):
    template_name = 'login_page.html'

    # def get_success_url(self):
    #     return reverse_lazy("user home page")
    # success_url = reverse_lazy("user home page")
    def get_success_url(self):

        if self.success_url:
            return self.success_url
        return reverse('user home page', kwargs = {
                'pk': self.request.user.id,
        }
                       )

    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #     next = self.request.GET.get('next', None)
    #     if next:
    #         return next
    #     return reverse('index.html', kwargs = {
    #             'pk': self.request.user.pk,
    #     })


class UserLogOutView(auth_views.LogoutView):
    next_page = 'welcome page'

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     messages.add_message(request, messages.INFO, 'Successfully logged out.')
    #     return response


# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("welcome page")


class EditUserProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'profile_edit.html'
    form_class = EditUserProfileBasicInfoForm

    # success_url = reverse_lazy('user home page')
    # fields = ('first_name', "last_name", "age", 'gender', 'profile_image')

    def get_success_url(self):
        return reverse('user home page', kwargs = {
                "pk": self.request.user.pk,
        })


class DeleteUserProfileView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'delete_account.html'
    model = UserModel
    success_url = reverse_lazy('welcome page')
    form_class = DeleteUserProfileBasicInfoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_detail'] = Profile.objects.get(pk = self.request.user.pk)
        return context


class UserPasswordResetView(auth_views.PasswordResetView):

    template_name = 'password_reset.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "password_reset_done.html"


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "password_reset_complete.html"

# class MultipleFormsView(FormMixin):
#     template_name = "template_name = 'delete_account.html"
#     form_classes = {'user_info': DeleteUserProfileBasicInfoForm,
#                     'user_profile': EditUserProfileBasicInfoForm,
#                     }
#
#     success_urls = {
#         'user_info': reverse_lazy('welcome page'),
#
#     }
#
#     def get_forms(self, form_classes):
#         return dict([(key, klass(**self.get_form_kwargs())) \
#                      for key, klass in form_classes.items()])
