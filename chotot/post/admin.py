from django.contrib import admin
from . import models

admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Image)
admin.site.register(models.ReportPost)
# Register your models here.
