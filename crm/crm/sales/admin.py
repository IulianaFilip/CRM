from django.contrib import admin

from .models import Accounts, Contacts, Deals, Leads

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ('lead', 'status', 'email', 'phone', 'owner')
    list_filter = ('status', 'owner')
    search_fields = ('lead', 'email', 'phone', 'owner')
    
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact', 'email', 'phone', 'priority')
    list_filter = ('priority',)
    search_fields = ('contact', 'email', 'phone')
    
@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('account', 'email', 'phone')
    search_fields = ('account', 'email', 'phone')
    
@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ('deal', 'owner', 'contact', 'account', 'stage', 'value')
    list_filter = ('stage', 'owner')
    search_fields = ('deal', 'owner', 'contact', 'account', 'stage', 'value')
