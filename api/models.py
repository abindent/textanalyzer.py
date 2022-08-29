from django.db import models
from django.db.models.fields import EmailField, CharField, TextField, AutoField, DateTimeField


# Create your models here.


class Contact(models.Model):
    sno = AutoField(primary_key=True)
    name = CharField(max_length=255)
    phone = CharField(max_length=30)
    email = EmailField(max_length=100)
    content = TextField()
    timeStamp = DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email