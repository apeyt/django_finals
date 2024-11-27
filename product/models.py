from django.db import models

# Create your models here.

class Employee(models.Model):
    # price = models.FloatField()
    # name = models.CharField(max_length=32)
    # description = models.CharField(max_length=200)
    # image_src = models.CharField(max_length=255 , blank=True , null=True)
    # # quantity
    

    # def __str__(self):
    #     return f'{self.pk} {self.name} - {self.price}'
    
    name = models.CharField(max_length=50, blank=True , null=True)
    department = models.CharField(max_length=30, blank=True , null=True)
    position = models.CharField(max_length=30, blank=True , null=True)
    hireDate = models.CharField(max_length=50, blank=True , null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True , null=True)
    email = models.EmailField(max_length=254, blank=True , null=True)
    contact = models.FloatField(max_length=30, blank=True , null=True)

    def __str__(self):
        return f'{self.name} - {self.department} - {self.position}'

