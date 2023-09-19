from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.models import Devices
from backend.serializers import DeviceDetailsSerializer
from backend.connect_database import connect_to_postgresql, execute_query

# Create your views here.

class DeviceDetailsViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DeviceDetailsSerializer

    @action(detail=True, methods=['GET'])
    def weather_data(self, request, pk=None):
        device = get_object_or_404(Devices, pk=pk)
        weather_data_instances = WeatherData.objects.filter(device=device)
        serializer = WeatherDataSerializer(weather_data_instances, many=True)
        return Response(serializer.data)

    def list(self, request):
        # Replace these values with your database details and SQL query
        host = "localhost"
        database = "backend"
        user = "postgres"
        password = "cliametnet2024"
        query = "SELECT * FROM weather_data"
        # Connect to the PostgreSQL database
        connection = connect_to_postgresql(host, database, user, password)

        if connection:
            # Execute the SQL query
            result = execute_query(connection, query)

            if result:
                # Do something with the result
                # Here, we'll convert it to a list of dictionaries
                data = [{'name': row[0], 'description': row[1]} for row in result]
                return Response(data)

        return Response([])  # Return an empty response if there's an error
