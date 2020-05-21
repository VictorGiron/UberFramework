from rest_framework.serializers import ModelSerializer, SerializerMethodField
from travels.models import Destination, Vehicle, Travel
from users.models import Client, Driver

#Usersserializers
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'gender']

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'gender', 'email']

#destination
class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'price']

class DestinationDetailSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'price']

#vehicle
class VehicleSerializer(ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'plates', 'color', 'driver']

class VehicleDriverSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'driver']

class VehicleDetailSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'plates', 'color', 'driver']
        depth = 1

#travel
class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
        fields = ['id', 'client', 'destination', 'vehicle']

class TravelDetailSerializer(ModelSerializer):
    vehicle = VehicleSerializer()
    destination = DestinationSerializer()
    client = ClientSerializer()

    class Meta:
        model = Travel
        fields = ['id', 'destination', 'client', 'vehicle']