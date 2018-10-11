from django.urls import path
from .views import ListCreateEmployeeView, LoginView, RegisterUsers

urlpatterns = [
    path('employee/', ListCreateEmployeeView.as_view(), name="employee-list-create"),
    path('', ListCreateEmployeeView.as_view(), name="employee-list-create"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
]