from django.db import models


from django.db import models

class Person(models.Model):
    person_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
# Create your models here.
