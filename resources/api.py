from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rbac.decorators import permission_required
from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Document.object.all()
	serializer_class = DocumentSerializer

	@permission_required('document','read')
	def list(self,request,*args,**kwargs):
		return super().create(request,*args,**kwargs)

	@permission_required('document', 'create')
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	@permission_required('document', 'read')
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@permission_required('document', 'update')
	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@permission_required('document', 'delete')
	def destroy(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)