"""Defines URL patterns for accounts."""
from django.urls import path
from . import views

# app_name is harmless to keep; we're not namespacing the include above
# app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),
    # optional: path("", views.index, name="index"),
]
