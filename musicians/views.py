from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from musicians.models import Musician
from musicians.serializers import MusicianSerializer
from rest_framework import filters
from django_filters import rest_framework

BEATLES = [
    {
      "first_name": "John",
      "last_name": "Lennon",
      "instrument": "Guitar"
    },
    {
      "first_name": "Paul",
      "last_name": "McCartney",
      "instrument": "Bass"
    },
    {
      "first_name": "George",
      "last_name": "Harrison",
      "instrument": "Guitar"
    },
    {
      "first_name": "Ringo",
      "last_name": "Star",
      "instrument": "Drums"
    },

]

class MusicianFilter(rest_framework.FilterSet):
    first_name = rest_framework.CharFilter(lookup_expr='icontains')
    last_name = rest_framework.CharFilter(lookup_expr='iexact')


    class Meta:
        model = Musician
        fields = [
            'instrument',
        ]


class MusicianViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['instrument']
    filter_class = MusicianFilter


    @action(detail=False)
    def create_beatles(self, request):
        beatles_in_db = []
        for beatle in BEATLES:
            db_beatle, created = Musician.objects.get_or_create(
                first_name=beatle['first_name'],
                last_name=beatle['last_name'],
                defaults=beatle,
            )
            beatles_in_db.append(db_beatle)

        serializer = self.get_serializer(beatles_in_db, many=True)
        # return Response({})
        return Response(serializer.data)



    # def get_queryset(self):
    #     user = self.request.user
    #     return user.purchase_set.all()









'''
class MusicianDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''
