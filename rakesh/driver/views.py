from driver.models import Driver
from rest_framework import generics
from rest_framework.response import Response
 
from driver.serializers import DriverSerializer
 
 
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = DriverSerializer
    
	def get_queryset(self):
		return Driver.objects.all()
