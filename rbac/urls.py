from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import RoleViewSet, ResourceTypeViewSet, AccessPermissionViewSet

router = DefaultRouter()
router.register('roles', RoleViewSet)
router.register('resource-types', ResourceTypeViewSet)
router.register('permissions', AccessPermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]