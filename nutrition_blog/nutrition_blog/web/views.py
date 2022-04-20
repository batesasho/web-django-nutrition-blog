from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.views import generic as views
from django.views.generic import detail as detail_mixin

from nutrition_blog.web.models import Articles

UserModel = get_user_model()


class WelcomePageView(views.TemplateView):
    template_name = 'welcome_page.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[] =...
    #     return context

    # when user logged in then redirect to its home page (user's index).
    # def dispatch check whether the user has access to the specific view, that's in-built !!!!
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user home page', pk = self.request.user.pk)
        return super().dispatch(request, *args, **kwargs)


#
class UserDetailView(detail_mixin.SingleObjectMixin,
                     views.ListView):  # auth_mixins.LoginRequiredMixin, views.DetailView
    model = UserModel
    template_name = 'index.html'
    paginate_by = 3
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset = UserModel.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usermodel'] = self.object

        return context

    def get_queryset(self):
        return self.object.articles_set.all()

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs['pk']
    #     context = super().get_context_data(**kwargs)
    #     profile = Profile.objects.get(pk = pk)
    #     context['profile'] = profile
    #     return context

    # def get_queryset(self):
    #     query = super().get_queryset()
    #     user_pk = self.kwargs['pk']
    #     current_user = get_object_or_404(UserModel, pk = user_pk)
    #     profile = query.filter(user = current_user)
    #     return profile


class AboutTemplateView(views.TemplateView):
    template_name = 'about_page.html'


class ArticleUserView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = "specific_article_view.html"
    model = Articles

