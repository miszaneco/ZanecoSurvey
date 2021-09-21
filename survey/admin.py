from django.contrib import admin
from .models import Survey, Sub_Rating

# Register your models here.
admin.site.register(Survey)
admin.site.register(Sub_Rating)

admin.site.site_title = 'Zaneco App'
admin.site.site_header = 'Zaneco App'