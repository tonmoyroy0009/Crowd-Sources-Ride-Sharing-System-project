from django.contrib import admin
from .models import Payment, Transition, CashInOrOut


admin.site.register(Payment)
admin.site.register(Transition)
admin.site.register(CashInOrOut)
