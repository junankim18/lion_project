from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    auth = models.FileField(verbose_name='인증파일',
                            upload_to='account/', blank=True, null=True)

    def __str__(self):
        return self.username
