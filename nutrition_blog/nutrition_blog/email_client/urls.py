from django.urls import path

from nutrition_blog.email_client.views import SuccessEmailSentView, ConsultantView

urlpatterns = (
        path('consultant/', ConsultantView.as_view(), name = 'consultant'),
        path('success/', SuccessEmailSentView.as_view(), name = 'success'),
)
