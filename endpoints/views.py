from django.shortcuts import render
from rest_framework import generics
from .models import EmployeeModel
from .serializer import EmployeeSerializer
class EmployeeView(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'