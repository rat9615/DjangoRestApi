from BankApi.viewsets import BranchesApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register('branches', BranchesApi)
