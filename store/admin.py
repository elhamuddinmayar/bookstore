from atexit import register
from django.contrib import admin
from .models import *


admin.site.register(Bookstore)
admin.site.register(Collection)