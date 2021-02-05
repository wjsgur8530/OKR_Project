from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# class Month(models.Model):
#     Month_choices = [
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#     ]
#     month = models.CharField(max_length=20, choices=Month_choices, blank=True)


class Board(models.Model):
    month = models.CharField(max_length=20, null=True)
    context = models.CharField(max_length=300, null=True)
    expect = models.FloatField(default=0)
    startdate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    enddate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    time = models.IntegerField(default=0)
    problem = models.CharField(max_length=70, null=True)
    result = models.FloatField(default=0)
    solution = models.CharField(max_length=20, null=True)
    team = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=20, null=True)
    task=models.CharField(max_length=20, null=True)
    num=models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name= 'auths', on_delete=models.DO_NOTHING, blank=True, null=True)

class Company(models.Model):
    title = models.CharField(max_length=20, null=True)
    context = models.CharField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

class Personalgoal(models.Model):
    person = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=20, null=True)
    context = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=20, null=True)
    month = models.CharField(max_length=20, null=True)

class Departmentgoal(models.Model):
    department = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=20, null=True)
    context = models.CharField(max_length=50, null=True)
    month = models.CharField(max_length=20, null=True)

class Classification(models.Model):
    num = models.IntegerField(default=0)
    title = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=20, null=True)
    month = models.CharField(max_length=20, null=True)
