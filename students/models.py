from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField(unique=True) 
    name = models.CharField(max_length=60)
    student_class = models.CharField(max_length=60)
    section = models.CharField(max_length=60)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.roll_no} - {self.name}"