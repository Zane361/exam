from django.contrib import admin
from . import models

admin.site.register(models.Home)
admin.site.register(models.AboutUs)
admin.site.register(models.Service)
admin.site.register(models.Blog)
admin.site.register(models.Contact)

