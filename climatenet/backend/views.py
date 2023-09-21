import psycopg2
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import DeviceSerializer

class DeviceDetailView(generics.ListAPIView):  # Change to ListAPIView
    serializer_class = DeviceSerializer

    def get_queryset(self):
        device_id = self.kwargs.get('device_id')

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

            # Execute a query to retrieve the last 10 rows from the corresponding table
            query = f"SELECT * FROM {table_name} ORDER BY time DESC LIMIT 10;"
            cursor.execute(query)

            # Fetch all 10 rows
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

    def list(self, request, *args, **kwargs):  # Use list method for ListAPIView
        queryset = self.get_queryset()

        if not queryset:
            return Response({'detail': 'No data found for this device.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DeviceSerializer(data=queryset, many=True)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
