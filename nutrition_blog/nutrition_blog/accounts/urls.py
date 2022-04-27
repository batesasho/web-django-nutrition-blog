from django.urls import path


from nutrition_blog.accounts.views import UserRegistrationView, UserLoginView, EditUserProfileView, \
    DeleteUserProfileView, UserLogOutView, UserPasswordResetView, \
    UserPasswordResetConfirmView, UserPasswordResetDoneView, UserPasswordResetCompleteView

urlpatterns = (
        path('register/', UserRegistrationView.as_view(), name = 'user register'),

        path('login/', UserLoginView.as_view(), name = 'user login'),
        path('logout/', UserLogOutView.as_view(), name = "user logout"),


        path('edit_profile/<int:pk>/', EditUserProfileView.as_view(), name = 'edit profile'),
        path('delete_profile/<int:pk>', DeleteUserProfileView.as_view(), name = 'delete profile'),



        path('password_reset/', UserPasswordResetView.as_view(), name = "password_reset"),
        path('password_reset/confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(),
             name = "password_reset_confirm"),
        path('password_reset/done', UserPasswordResetDoneView.as_view(), name = "password_reset_done"),
        path('password_reset/complete', UserPasswordResetCompleteView.as_view(), name = "password_reset_complete"),
)
