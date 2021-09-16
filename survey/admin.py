from django.contrib import admin
from .models import sub_rating, survey

# Register your models here.
admin.site.register(survey)
admin.site.register(sub_rating)

admin.site.site_title = 'Zaneco App'
admin.site.site_header = 'Zaneco App'