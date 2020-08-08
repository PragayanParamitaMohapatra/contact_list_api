from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    country=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
    contact_picture=models.URLField(null=True)
    is_favourite=models.BooleanField(default=True)
     
    class Meta:
        verbose_name='contact'
        verbose_name_plural='contacts'

    def __str__(self):
        return self.owner
