from django.contrib.auth.models import AbstractUser
from django.db import models


class CustonUser(AbstractUser):
    name = models.CharField('Nome', max_length=50)
    cell = models.CharField('Telefone', max_length=11)
