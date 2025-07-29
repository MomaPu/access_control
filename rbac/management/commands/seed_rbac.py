from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from accounts.models import CustomUser
from rbac.models import ResourceType, Role, AccessPermission

# Заполнение данными
class Command(BaseCommand):
	help = 'Seeds RBAC system with test data'

	def handle(self, *args, **options):
		#Очищаем данные
		ResourceType.objects.all().delete()
		Role.objects.all().delete()
		AccessPermission.objects.all().delete()

		# Создаем типы ресурсов
		document_type = ResourceType.objects.create(
			name='document',
			description='Документы'
		)

		report_type = ResourceType.objects.create(
			name='report',
			description='Отчеты'
		)

		# Создаем роли
		admin_role = Role.objects.create(
			name='admin',
			description='Администратор'
		)

		manager_role = Role.objects.create(
			name='manager',
			description='Менеджер'
		)

		user_role = Role.objects.create(
			name='user',
			description='Обычный пользователь'
		)

		# Назначем права
		# Админ имеет доступ ко всему
		AccessPermission.objects.create(
			role=admin_role,
			resource_type=document_type,
			can_read=True,
			can_write=True,
			can_delete=True
		)
		AccessPermission.objects.create(
			role=admin_role,
			resource_type=report_type,
			can_read=True,
			can_write=True,
			can_delete=True
		)

		# Менеджер создает и читает, но не удаляет
		AccessPermission.objects.create(
			role=manager_role,
			resource_type=document_type,
			can_read=True,
			can_write=True,
			can_delete=False
		)

		# Обычный пользователь может только читать документы
		AccessPermission.objects.create(
			role=user_role,
			resource_type=document_type,
			can_read=True,
			can_write=False,
			can_delete=False
		)

		self.stdout.write(self.style.SUCCESS('Successfully seeded RBAC data'))
