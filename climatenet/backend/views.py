from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from backend.models import Devices, WeatherData
from backend.serializers import DeviceDetailsSerializer, WeatherDataSerializer
import psycopg2

class DeviceDetailsViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DeviceDetailsSerializer

    def retrieve_device(self, request, pk=None):
        try:
            # Replace these values with your database details
            host = "climatenet.c8nb4zcoufs1.us-east-1.rds.amazonaws.com"
            database = "raspi_data"
            user = "postgres"
            password = "climatenet2024"

            # Create a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Determine the table name based on the device ID
            table_name = f"device{pk}"

            # Debug: Print the generated table name
            print("Generated Table Name:", table_name)

            # Replace this query with your SQL query
            query = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 10"

            # Debug: Print the executed SQL query
            print("Executed SQL Query:", query)

            # Execute the SQL query
            cursor.execute(query)

            # Fetch all the results
            results = cursor.fetchall()

            data_list = []
            for result in results:
                # Debug: Print the result
                print("Result:", result)

                data = {
                    'time': result[1],
                    'light': result[2],
                    'temperature': result[3],
                    'pressure': result[4],
                    'humidity': result[5],
                    'pm1': result[6],
                    'pm2_5': result[7],
                    'pm10': result[8],
                    'co2': result[9],
                    'speed': result[10],
                    'rain': result[11],
                    'direction': result[12],
                }
                data_list.append(data)

            # Debug: Print the data_list
            print("Data List:", data_list)

            return Response(data_list)

        except psycopg2.Error as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            cursor.close()
            connection.close()

