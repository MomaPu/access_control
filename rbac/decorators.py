from functools import wraps
from django.http import HttpResponseForbidden

# Декоратор для доступа
def permission_required(resource_type,permission_type):
	def decorator(view_func):
		@wraps(view_func)
		def wrapped_view(request,*args,**kwargs):
			if not request.user.has_perm(f'rbac.{permission_type}_{resource_type}'):
				return HttpResponseForbidden
			return view_func(request,*args,**kwargs)

		wrapped_view.required_permission = {
			'resource_type' : resource_type,
			'permission_type' : permission_type,
		}
		return wrapped_view()
	return decorator()