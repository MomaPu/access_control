from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):

	email = models.EmailField(_('email_address'), unique=True)
	first_name = models.CharField(_('first_name'), max_length=150)
	last_name = models.CharField(_('last_name'), max_length=150)
	middle_name = models.CharField(_('middle_name'), max_length=150, blank = True)
	is_active = models.BooleanField(_('active'), default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','first_name','last_name']

	class Meta:
		verbose_name = _('Пользователь')
		verbose_name_plural = _('Пользователи')

	def __str__(self):
		return f"{self.last_name}{self.first_name}{self.middle_name or ''}".strip()



