from django.contrib import admin

# Register your models here.
from .models import Query,Solution,Category

admin.site.register(Query)
admin.site.register(Solution)
admin.site.register(Category)
# admin.site.register(Preference)
