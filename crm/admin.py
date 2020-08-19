from django.contrib import admin

from crm.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'phone_number')}),
        ('Time machine', {
            'classes': ('collapse',),
            'fields': ('created', 'updated')
        })
    )
    list_display = ['name', 'phone_number']
