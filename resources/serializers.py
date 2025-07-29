from rest_framework import serializers
from .models import Document
# Сериализация продукта
class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ['id', 'title', 'content', 'owner', 'created_at', 'updated_at', 'is_public']
		read_only_fields = ['owner', 'created_at', 'updated_at']