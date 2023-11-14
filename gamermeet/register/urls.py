from django.urls import path
from .views import UserRegisterView, Settings, EditUserProfile


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("settings/", Settings.as_view(), name="settings"),
    path("edit_profile/", EditUserProfile.as_view(), name="edit_profile"),
]