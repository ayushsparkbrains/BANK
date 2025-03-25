from django.db import models

class Bank(models.Model):
    bank_code = models.CharField(max_length=10, unique=True)
    bank_name = models.CharField(max_length=255)
    swift_ifsc_code = models.CharField(max_length=20, blank=True, null=True) 
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bank_code} - {self.bank_name}"
    


    
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name