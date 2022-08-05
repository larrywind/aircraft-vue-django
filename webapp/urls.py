from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.home_page),
    path("test/", views.test),
]
