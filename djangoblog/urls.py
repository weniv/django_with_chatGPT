from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("", include("main.urls", namespace="main")),
]
