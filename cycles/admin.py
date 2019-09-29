from .models import Location, Cycle, Dropcycle, Pickcycle
from django.contrib import admin


admin.site.register(Cycle)
admin.site.register(Location)
admin.site.register(Dropcycle)
admin.site.register(Pickcycle)
