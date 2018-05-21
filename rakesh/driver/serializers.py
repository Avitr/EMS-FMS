from rest_framework import serializers
from driver.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id','first_name', 'last_name', 'age', 'adhar_number', 'phone_number')

