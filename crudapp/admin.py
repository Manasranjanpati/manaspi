from django.contrib import admin
from .models import Applicant, Designation

admin.site.register(Designation)
admin.site.register(Applicant)