

# Register your models here.
from django.contrib import admin

from .models import Booker
from .models import Newsletter


admin.site.register(Booker)
admin.site.register(Newsletter)