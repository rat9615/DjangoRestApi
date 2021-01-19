from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .serializers import BranchesSerialize
from .models import Branches


class BranchesApi(viewsets.ModelViewSet):
    queryset = Branches.objects.all().order_by('ifsc')
    serializer_class = BranchesSerialize
    filter_backends = [SearchFilter]
    search_fields = ['ifsc', 'bank__id', 'branch',
                     'address', 'city', 'district', 'state']
