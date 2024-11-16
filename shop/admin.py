from django.contrib import admin
from . import models

admin.site.site_header = "Заголовок"
admin.site.site_title = "Uslugi"
admin.site.index_title = "Описание услуг"


admin.site.register(models.Category)
admin.site.register(models.Course)

