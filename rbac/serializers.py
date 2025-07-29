from rest_framework import serializers
from .models import Role, ResourceType, AccessPermission

# Сериализация для для rbac
class ResourceTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResourceType
		fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = '__all__'

class AccesPermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccessPermission
		fields = '__all__'