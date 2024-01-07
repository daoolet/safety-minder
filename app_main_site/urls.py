from django.urls import path

from . import views

app_name = 'app_main_site'

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("profile/update", views.update_profile, name="update_profile"),

    path('registration/', views.custom_registration, name='registration'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]