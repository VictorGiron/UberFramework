from django.urls import path
from users import views

urlpatterns = [
    path('client/', views.ListCreateClient.as_view(), name='clients'),
    path('client/<int:pk>/', views.RetrieveUpdateDestroyClient.as_view(), name='client'),

    path('driver/', views.ListCreateDriver.as_view(), name='drivers'),
    path('driver/<int:pk>/', views.RetrieveUpdateDestroyDriver.as_view(), name='driver'),
]
