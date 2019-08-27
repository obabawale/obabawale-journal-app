from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path("auth/login", views.login_view, name="login_custom" ),
    path("auth/logout", views.logout_view, name="logout_custom" ),
    path("auth/signup", views.signup_view, name="signup_custom" ),
]
