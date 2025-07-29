from django.db import models
from django.contrib.auth.models import Permission, Group
class ResourceType(models.Model):
	name = models.CharField(max_length=50,unique=True)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Тип ресурса'
		verbose_name_plural = 'Типы ресурсов'

class Resource(models.Model):
	name = models.CharField(max_length=50)
	resource_type = models.ForeignKey(ResourceType,on_delete=models.PROTECT)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Ресурс'
		verbose_name_plural = 'Ресурсы'

class Role(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	permissions = models.ManyToManyField(Permission, blank=True)
	groups = models.ManyToManyField(Group, blank=True)

	class Meta:
		verbose_name = 'Роль'
		verbose_name_plural = 'Роли'


class AccessPermission(models.Model):
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
	can_read = models.BooleanField(default=False)
	can_write = models.BooleanField(default=False)
	can_delete = models.BooleanField(default=False)

	class Meta:
		unique_together = ('role', 'resource_type')