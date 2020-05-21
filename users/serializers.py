from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Client, Driver
from travels.models import Travel, Vehicle, Destination

#TravelsSerializers
class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'price']

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'gender', 'email', 'dpi']

class DriverVehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'plates', 'color']

class VehicleSerializer(ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'plates', 'color', 'driver']

class TravelDetailSerializer(ModelSerializer):
    vehicle = VehicleSerializer()
    destination = DestinationSerializer()

    class Meta:
        model = Travel
        fields = ['id', 'destination', 'vehicle']

class TravelSerializer(ModelSerializer):
    class Meta:
        model = Travel
        fields = ['id', 'destination', 'client']

#Client
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'gender', 'email']

class ClientDetailSerializer(ModelSerializer):
    travels = TravelDetailSerializer(source='travel_set', many=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'gender', 'travels']

#Driver

class DriverDetailSerializer(ModelSerializer):
    vehicle = DriverVehicleSerializer(source='vehicle_set', many=True )

    class Meta:
        model = Driver
        fields = ['id', 'name', 'gender', 'email', 'vehicle']


