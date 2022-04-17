from django.urls import path

from nutrition_blog.web.views import WelcomePageView, UserDetailView, AboutTemplateView

urlpatterns = (
        path('', WelcomePageView.as_view(), name = 'welcome page'),
        path('index/<int:pk>/', UserDetailView.as_view(), name = 'user home page'),
        path('about/', AboutTemplateView.as_view(), name = 'about page'),

)
