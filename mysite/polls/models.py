from django.db import models
from django.db.models.enums import IntegerChoices
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class User(models.Model):
    name = CharField(max_length=10)
    age = IntegerField()
    job = CharField(max_length=20)

class Text(models.Model):
    title = CharField(max_length=20)
    body = CharField(max_length=500)
    user = models.ForeignKey(User, related_name="texts", on_delete=models.PROTECT)