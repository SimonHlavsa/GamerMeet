from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("discover/", views.discover, name="discover"),
	path("profile/", views.profile, name="profile"),
	path("contacts/", views.contacts, name="contacts"),
	path("like/<int:pk>", views.LikeView, name="like_user"),
	path("dislike/<int:pk>", views.DislikeView, name="dislike_user"),
]