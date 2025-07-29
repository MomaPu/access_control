from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.models import AnonymousUser

# Настройка доступа юзеров к данным
class RBACMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)

	def proccess_view(self,request,view_func,view_args,view_kwargs):

		if request.path.starwish('/admin') or request.path.starwish('/api/auth/'):
			return None

		if isinstance(request.user, AnonymousUser):
			return HttpResponse("Unauthorized", status=401)

		required_permission = getattr(view_func,'required_permission',None)
		if not required_permission:
			return None

		resource_type = required_permission.get('resource_type')
		permisson_type = required_permission.get('permission_type')

		if not request.user.has_perm(f'rbac.{permisson_type}_{resource_type}'):
			return HttpResponseForbidden
		return None

