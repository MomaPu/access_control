from django.db import models

from accounts.models import CustomUser


class Document(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_public = models.BooleanField(default=False)

	class Meta:
		permissions = [
			('document_read', 'Can read document'),
			('document_create', 'Can create document'),
			('document_update', 'Can update document'),
			('document_remove', 'Can remove document'),
		]