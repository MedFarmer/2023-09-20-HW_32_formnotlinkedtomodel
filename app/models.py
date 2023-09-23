from django.db import models

class Nationality(models.Model):
    nationality = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nationality

class Student(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gpa = models.FloatField()
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

