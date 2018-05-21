from django.db import models

class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    age=models.IntegerField()
    class Meta:
        ordering = ('created',)