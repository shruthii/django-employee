from django.db import models
from django.utils import timezone
#from django.core.urlresolver import reverse
from django.urls import reverse
# Create your models here.

class EmpDetailsModel(models.Model):
    gender_det = (('M','Male'),
                    ('F','Female'),)
    status_d = (('A','Active'),('I','Inactive'))
    FullName = models.TextField()
    DOB = models.DateTimeField(default=timezone.now())
    PermanentAddress = models.CharField(max_length=200)
    Dateofjoining = models.DateTimeField(default=timezone.now())
    Designation = models.TextField()
    Department = models.TextField()
    EmployeeId = models.TextField(primary_key=True)
    
    EmailId = models.EmailField()
    Gender = models.TextField(max_length=1,choices=gender_det)
    Phonenumber = models.TextField(max_length=10)
    Status = models.TextField(choices=status_d)                                    #(Active, Inactive)

    def get_absolute_url(self):
        return reverse("List")

    def __str__(self):
        return self.FullName
