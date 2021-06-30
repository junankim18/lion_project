from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(_(""), max_length=254)
    auth = models.FileField(verbose_name='인증파일', upload_to='account/')
