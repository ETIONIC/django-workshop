from rest_framework import serializers
from musicians.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


'''

from musicians.serializers import MusicianSerializer
serializer = MusicianSerializer()
print(repr(serializer))


'''
