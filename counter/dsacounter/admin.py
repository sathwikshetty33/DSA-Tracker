from django.contrib import admin
from .models import progress, rooms, studying,teacher

admin.site.register(progress)
admin.site.register(rooms)
admin.site.register(studying)
admin.site.register(teacher)