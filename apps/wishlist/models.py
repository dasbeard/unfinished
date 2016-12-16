from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import Users


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField('loginReg.Users', related_name='userItems')
