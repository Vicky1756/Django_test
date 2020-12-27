from django.db import models

# Create your models here.
import uuid


def id_f():
    return uuid.uuid4().hex[:20]


class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +","+self.location


class Student(models.Model):

    school = models.ForeignKey(School, related_name="school", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    identification = models.CharField(
        max_length=20, default=id_f, primary_key=True, editable=False)

    def __str__(self):
    
        return self.firstname + " " + self.lastname +"," + self.identification