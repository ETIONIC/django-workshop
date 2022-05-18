from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from musicians.models import Musician
from musicians.serializers import MusicianSerializer

@csrf_exempt
def musician_list(request):
    if request.method == 'GET':
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MusicianSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def musician_detail(request, pk):
    try:
        snippet = Musician.objects.get(pk=pk)
    except Musician.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MusicianSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MusicianSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
