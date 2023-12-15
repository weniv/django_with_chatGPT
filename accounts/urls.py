from django.urls import path
from . import views

app_name = "accounts"  # 앱 이름 설정

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile/<int:id>/", views.profile_view, name="profile"),
]
