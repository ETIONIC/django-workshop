from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from musicians.models import Musician
from musicians.serializers import MusicianSerializer


@api_view(['GET', 'POST'])
def musician_list(request):
    """
    List all code musicians, or create a new musician.
    """
    if request.method == 'GET':
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def musician_detail(request, pk):
    """
    Retrieve, update or delete a code musician.
    """
    try:
        musician = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
