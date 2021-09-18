from django.core.exceptions import ValidationError
from django.db import models


def validate_file_extension(value):
	"""
	Проверка расширение загружаемого файла
	:param value:
	:return:
	"""
	if not (value.name.endswith('.txt')):
		raise ValidationError(u'Неверное расширение файла, должно быть .txt')


class Document(models.Model):
	description = models.CharField(max_length=255, blank=True, verbose_name="Описание файла")
	document = models.FileField(upload_to='documents/', verbose_name="Имя файла",
	                            validators=[validate_file_extension])
	uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Время загрузки файла")


