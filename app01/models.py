from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=16)
    age=models.IntegerField()
    salary=models.IntegerField()
    province=models.CharField(max_length=31)
    dept=models.CharField(max_length=16)
    def __str__(self):
        return self.name


class Employee2(models.Model):
    name=models.CharField(max_length=16)
    age=models.IntegerField()
    salary=models.IntegerField()
    province=models.CharField(max_length=31)
    dept=models.ForeignKey(to="Dept")
    def __str__(self):
        return self.name
class Dept(models.Model):
    name=models.CharField(max_length=16)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)
    books=models.ManyToManyField(to="Book")
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=32)
    def __str__(self):
        return self.title