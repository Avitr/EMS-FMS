from patient.models import Patient
from rest_framework import generics
from rest_framework.response import Response
 
from patient.serializers import PatientSerializer
 
 
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PatientSerializer
    
	def get_queryset(self):
		return Patient.objects.all()
