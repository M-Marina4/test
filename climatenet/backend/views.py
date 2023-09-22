import psycopg2
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import DeviceSerializer
from datetime import datetime, timedelta

class DeviceDetailView(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        device_id = self.kwargs.get('device_id')

        # Get start_time and end_time from query parameters, if specified
        start_time_str = self.request.query_params.get('start_time_str')
        end_time_str = self.request.query_params.get('end_time_str')

        # If start_time and end_time are not specified, calculate the date range for the last 24 hours of the previous day
        if not (start_time_str and end_time_str):
            end_time = datetime.now() - timedelta(days=1)
            start_time = end_time - timedelta(hours=24)
            start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
            end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')

        # Define the PostgreSQL connection parameters
        host = "climatenet.c8nb4zcoufs1.us-east-1.rds.amazonaws.com"
        database = "raspi_data"
        user = "postgres"
        password = "climatenet2024"

        try:
            # Create a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Construct the table name based on the device_id
            table_name = f'device{device_id}'

            # Execute a query to retrieve rows within the specified time range
            query = f"SELECT * FROM {table_name} WHERE time >= %s AND time <= %s ORDER BY time DESC;"
            cursor.execute(query, (start_time_str, end_time_str))

            # Fetch all rows within the time range
            rows = cursor.fetchall()

            # Check if any rows were found
            if rows:
                # Convert the rows into a list of dictionaries
                device_data = []
                for row in rows:
                    device_data.append({
                        'time': row[1],
                        'light': row[2],
                        'temperature': row[3],
                        'pressure': row[4],
                        'humidity': row[5],
                        'pm1': row[6],
                        'pm2_5': row[7],
                        'pm10': row[8],
                        'co2': row[9],
                        'speed': row[10],
                        'rain': row[11],
                        'direction': row[12],
                    })

                return device_data
            else:
                return []

        except Exception as e:
            return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset:
            return Response({'detail': 'No data found for this device in the specified time range.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(data=queryset, many=True)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

