from django.contrib import admin

from apps.trade.models import Symbol, Journal


admin.site.register(Symbol)
admin.site.register(Journal)

