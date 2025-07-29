from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Role, ResourceType, AccessPermission
from .serializers import RoleSerializer, ResourceTypeSerializer, AccessPermissionSerializer

class IsSuperUser(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_superuser

class RoleViewSet(viewsets.ModelViewSet):
	queryset = Role.objects.all()
	serializer_class = RoleSerializer
	permission_classes = [IsSuperUser]

class ResourceTypeViewSet(viewsets.ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    permission_classes = [IsSuperUser]
class AccessPermissionViewSet(viewsets.ModelViewSet):
	queryset = AccessPermission.all()
	serializer_class = AccessPermissionSerializer
	permission_classes = [IsSuperUser]
