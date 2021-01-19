from rest_framework import viewsets
from .serializers import BranchesSerialize
from .models import Branches


class BranchesApi(viewsets.ModelViewSet):
    queryset = Branches.objects.raw(
        'select * from branches order by ifsc asc')
    serializer_class = BranchesSerialize
