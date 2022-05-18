from musicians.models import Musician
from musicians.serializers import MusicianSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MusicianList(APIView):
    """
    List all musicians, or create a new musician.
    """
    def get(self, request, format=None):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MusicianDetail(APIView):
    """
    Retrieve, update or delete a musician instance.
    """
    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        musician = self.get_object(pk)
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
