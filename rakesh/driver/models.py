from django.db import models

class Driver(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age=models.IntegerField()
    adhar_number = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=10)
    class Meta:
        ordering = ('created',)