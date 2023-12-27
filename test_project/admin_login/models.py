from django.db import models


# model_1

class manage_course(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    learning_hours = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title



# model_2

class manage_student(models.Model):
    
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    aadhar = models.IntegerField() 
    course = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
