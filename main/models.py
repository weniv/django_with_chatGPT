from django.db import models


class MainSetting(models.Model):
    site_name = models.CharField(max_length=100)
    welcome_message = models.TextField()

    def __str__(self):
        return self.site_name
