from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


class EmployeeAPI(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailsAPI(APIView):
    def get(self, request, pk=None):
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        obj = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        obj = get_object_or_404(Employee, pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

