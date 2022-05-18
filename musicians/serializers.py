from rest_framework import serializers
from musicians.models import Musician

class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    instrument = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()
        return instance


'''
from musicians.models import Musician
from musicians.serializers import MusicianSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

ringo = Musician(first_name='Ringo', last_name='Star', instrument='Drums')
ringo.save()



serializer = MusicianSerializer(ringo)
serializer.data



content = JSONRenderer().render(serializer.data)
content



import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)



serializer = MusicianSerializer(data=data)
serializer.is_valid()
serializer.save()
'''
