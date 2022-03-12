from django.contrib import admin

# Register your models here.
from tasks.models import Tasks,Team
admin.site.register(Tasks)
admin.site.register(Team)