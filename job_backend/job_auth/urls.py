from django.urls import path
from .views import *



## define urls patterns
urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
    path("reset-password/", ResetPasswordView.as_view()),
]
