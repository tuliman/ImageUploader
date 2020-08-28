from django.contrib import admin

# Register your models here.
from .models import Images,Size

admin.site.register(Images)
admin.site.register(Size)
