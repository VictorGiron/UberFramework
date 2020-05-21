from django.urls import path
from travels import views

urlpatterns = [
    path('destination/', views.ListCreateDestination.as_view(), name='destinations'),
    path('destination/<int:pk>/', views.RetrieveUpdateDestroyDestination.as_view(), name='destination'),

    path('vehicle/', views.ListCreateVehicle.as_view(), name='vehicles'),
    path('vehicle/<int:pk>/', views.RetrieveUpdateDestroyVehicle.as_view(), name='vehicle'),

    path('travels/', views.ListCreateTravel.as_view(), name='travels'),
    path('travels/<int:pk>/', views.RetrieveUpdateDestroyTravel.as_view(), name='travel'),
]
