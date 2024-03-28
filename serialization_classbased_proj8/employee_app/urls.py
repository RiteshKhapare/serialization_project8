from django.urls import path
from .views import EmployeeAPI, EmployeeDetailsAPI

urlpatterns = [
    path('emp/', EmployeeAPI.as_view()),
    path('emp/<int:pk>/', EmployeeDetailsAPI.as_view())
]
