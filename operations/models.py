from django.db import models

class student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName