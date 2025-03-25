from django.contrib import admin
from django.contrib import admin
from .models import Bank

    # @admin.register(Bank)
    # class BankAdmin(admin.ModelAdmin):
    #     list_display = ('bank_code', 'bank_name', 'country', 'swift_ifsc_code')
    #     search_fields = ('bank_code', 'bank_name', 'swift_ifsc_code')


admin.site.register(Bank)