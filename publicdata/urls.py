from django.urls import path
from .views import status_test, validate_test

urlpatterns = [
    path('status-test/', status_test, name='status_test'),
    path('validate-test/', validate_test, name='validate_test'),
]
