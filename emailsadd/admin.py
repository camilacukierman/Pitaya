

# Register your models here.
from django.contrib import admin

from .models import Booker,Survey,Newsletter


admin.site.register(Booker)
admin.site.register(Newsletter)
admin.site.register(Survey)