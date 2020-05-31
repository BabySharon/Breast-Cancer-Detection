from django.contrib import admin
from .models import Patient
from .models import userModel

admin.site.register(Patient)
admin.site.register(userModel)
