from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

class EmployeeView(APIView):

    def get(self , request , format=None):
        all_employees = Employee.objects.all().order_by('-id')
        serializer = EmployeeSerializer(all_employees , many=True)
        return Response({'ok': True , 'data': serializer.data}, status=200)

    def post(self , request , format=None):
        request_data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'message': 'Something went wrong' , 'error': serializer.errors})
        

    def patch(self , request , format=None):
        request_data = JSONParser().parse(request)
        employee_instance = Employee.objects.get(id=request_data['id'])
        serializer = EmployeeSerializer(employee_instance ,data=request_data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'message': 'Something went wrong' , 'error': serializer.errors})
        
    def delete(self , request, format=None):
        request_data = JSONParser().parse(request)
        try:
            object_instance = Employee.objects.get(id=request_data['id'])
            object_instance.delete()
            return Response({'ok': True , 'message': 'Deleted!' , 'product': request_data})
        except:
            return Response("Not Found!")
        
