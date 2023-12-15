from django.urls import path
from . import views

app_name = "blog"  # 앱 이름 설정

urlpatterns = [
    path("", views.post_list_view, name="post_list"),
    path("create/", views.post_create_view, name="post_create"),
    path("<int:id>/", views.post_detail_view, name="post_detail"),
    path("edit/<int:id>/", views.post_edit_view, name="post_edit"),
    path("delete/<int:id>/", views.post_delete_view, name="post_delete"),
]
