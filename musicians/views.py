from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from musicians.models import Musician
from musicians.serializers import MusicianSerializer
from rest_framework import filters
from django_filters import rest_framework



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
