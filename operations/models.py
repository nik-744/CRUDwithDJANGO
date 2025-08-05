from django.db import models

class department(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return f"{self.name}"

class student(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.email} - {self.age}- {self.department}"
        # return self.firstName

