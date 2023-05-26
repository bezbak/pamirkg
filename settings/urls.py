from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("tours/", tours, name="tours"),
    path("contact/", contact, name="contact"),
    path("gallery/", gallery, name="gallery"),
    path("photos/", photos, name="photos"),
    path("video/", video, name="video"),
    path("tour/<int:id>/", tour, name="tour"),
    # path("gallery/", gallery, name="gallery"),
]
