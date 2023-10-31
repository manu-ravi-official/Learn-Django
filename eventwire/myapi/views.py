from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EventImage, Event
from .serializers import EventSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class CustomEventCreate(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        # Check if the request has a 'name' field.
        if 'name' not in request.data:
            return Response({'message': 'Name field is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the request data.
        serializer = EventSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save the event.
        event = serializer.save()

        # Handle image uploads
        images = request.FILES.getlist('image')
        for image in images:
            EventImage.objects.create(event=event, image=image)

        # Return a success response.
        response_data = {'message': 'Event created successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Retrieve a list of events from the database.
        events = Event.objects.all()  # You may want to filter this based on your requirements.

        # Serialize the events data.
        serializer = EventSerializer(events, many=True)

        # Return the serialized data in the response.
        return Response(serializer.data, status=status.HTTP_200_OK)
