from django.contrib import admin
import api.models

# Register your models here.
admin.site.register(api.models.Profile)
admin.site.register(api.models.Project)
admin.site.register(api.models.Task)
admin.site.register(api.models.Document)
