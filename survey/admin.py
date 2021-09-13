from django.contrib import admin
from .models import survey

# Register your models here.
admin.site.register(survey)

admin.site.site_title = 'Zaneco App'
admin.site.site_header = 'Zaneco App'