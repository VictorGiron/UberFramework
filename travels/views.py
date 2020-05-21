from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from travels.models import Travel, Destination, Vehicle
from travels.serializers import TravelSerializer, TravelDetailSerializer, DestinationSerializer, DestinationDetailSerializer, VehicleSerializer, VehicleDetailSerializer

#Destination
class ListCreateDestination(ListCreateAPIView):
    queryset = Destination.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DestinationDetailSerializer
        elif self.request.method == 'POST':
            return DestinationSerializer

class RetrieveUpdateDestroyDestination(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DestinationDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return DestinationSerializer

#Vehicle
class ListCreateVehicle(ListCreateAPIView):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VehicleDetailSerializer
        elif self.request.method == 'POST':
            return VehicleSerializer

class RetrieveUpdateDestroyVehicle(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VehicleDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return VehicleSerializer

#Travel
class ListCreateTravel(ListCreateAPIView):
    queryset = Travel.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TravelDetailSerializer
        elif self.request.method == 'POST':
            return TravelSerializer

class RetrieveUpdateDestroyTravel(RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TravelDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return TravelSerializer