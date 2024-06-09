from django.urls import path
from .import views


urlpatterns = [
    path("",views.index,name="index"),
    path("bookstore/",views.bookstore,name="bookstore"),
    path("services/",views.services,name="services"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about")
]
