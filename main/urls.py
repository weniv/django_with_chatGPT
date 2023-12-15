from django.urls import path
from . import views

app_name = "main"  # 앱 이름 설정

urlpatterns = [
    path("", views.index, name="index"),
]
