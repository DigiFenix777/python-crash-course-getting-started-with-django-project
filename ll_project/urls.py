"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Custom accounts routes (e.g., register)
    path("accounts/", include("accounts.urls")),
    # Django's built-in auth (login/logout/password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")),

    path("learning_logs/", include("learning_logs.urls")),
    path("pizzas/", include("pizzas.urls")),
    path("meal_plans/", include("meal_plans.urls")),
    path("blog/", include("blog.urls")),
]
