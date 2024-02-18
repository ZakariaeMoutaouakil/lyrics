# Create your views here.
import json
import os

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapi.models import client


@api_view(['POST'])
def lyrics(request):
    if request.FILES.get('audio'):
        # Get the uploaded file
        file = request.FILES['audio']

        # Ensure the destination folder exists, create it if necessary
        destination_folder = os.path.join(settings.MEDIA_ROOT, 'tmp')
        os.makedirs(destination_folder, exist_ok=True)

        # Save the file to the destination folder
        file_path = os.path.join(destination_folder, file.name)
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Process the file
        result = client.predict(f"tmp/{file.name}")

        # Delete the file after processing
        os.remove(file_path)

        # Return a response
        return Response(json.loads(result), status=200)

    # Handle case when no file is provided
    return Response({'error': 'No file provided.'}, status=400)
