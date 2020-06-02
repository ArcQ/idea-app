from django.db import models
import uuid


class GenericModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Team(GenericModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(GenericModel):
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ideas(GenericModel):
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    people = models.ManyToManyField(Person)
