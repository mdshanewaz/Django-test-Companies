from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=100, null=True)
    about = models.TextField(null=True)
    type = models.CharField(max_length=100, null=True, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Garments', 'Garments')))
    date_created = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100, choices=(('CEO', 'CEO'), ('CTO', 'CTO'), ('SE', 'SE'), ('TecLead', 'TecLead')))
    about = models.TextField(null=True)

    def __str__(self):
        return self.name +'--'+ self.job_title

class Asset(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=(('Laptop', 'Laptop'), ('Phone', 'Phone'), ('Desktop', 'Desktop'), ('Bycycle', 'Bycycle'), ('Car', 'Car')))
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class DeviceLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField(default=timezone.now)
    checked_in_date = models.DateTimeField(null=True, blank=True)
    checked_out_condition = models.CharField(max_length=100)
    checked_in_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.checked_in_date
    

