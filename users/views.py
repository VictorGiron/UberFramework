from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import Client, Driver
from users.serializers import ClientSerializer, ClientDetailSerializer, DriverSerializer, DriverDetailSerializer

#Client
class ListCreateClient(ListCreateAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        elif self.request.method == 'POST':
            return ClientSerializer

class RetrieveUpdateDestroyClient(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return ClientSerializer

#Driver
class ListCreateDriver(ListCreateAPIView):
    queryset = Driver.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DriverDetailSerializer
        elif self.request.method == 'POST':
            return DriverSerializer

class RetrieveUpdateDestroyDriver(RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DriverDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return DriverSerializer
