from django.urls import path

from .views import *

urlpatterns = [
    path("", MainPage.as_view(), name="home"), # main.html
    path("signup/", SignUpPage.as_view(), name="signup"), # signup.html
    path("ref/", RefPage.as_view(), name="ref"), # ref.html
    path("logout/", logout_user, name="logout"), # -
    path("error/", error, name="error"), # -
    path("user/<int:id>", PesonalAccount.as_view(), name="user"), # user.html
    path("rate/", RatePage.as_view(), name="rate"), # rate.html
    path('login/', LoginUser.as_view(), name='login'), # login.html
    path('generate-code/', GenerateCode.as_view(), name='generate-code'), # generate.html
    path('edit-admin-page/', EditAdmin.as_view(), name='edit-admin'), # editadmin.html
]

