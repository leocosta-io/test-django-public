from django.db import models


### Task 1: Create here the Model Course here
class Course(models.Model):
    None


### Task 1 - End


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, help_text="ISO 639-1 code")

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    username = models.CharField(max_length=300)
    certid = models.CharField(max_length=20)
    languages = models.ManyToManyField(Language)

    ### Task 2: Create here the courses field using ManyToManyField

    ### Task 2 - End

    def __str__(self):
        return self.name
