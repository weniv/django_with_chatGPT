from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True
    )
