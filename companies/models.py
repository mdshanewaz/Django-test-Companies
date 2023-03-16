from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Asset(models.Model):
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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
    

