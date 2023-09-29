from django.contrib import admin

from .models import Accounts, Contacts, Deals, Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ("lead", "status", "email", "phone", "owner")
    search_fields = ("lead", "owner")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("contact", "email", "phone", "priority")
    search_fields = ("contact", "phone")


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ("account", "email", "phone")
    search_fields = ("account", "phone")


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ("deal", "owner", "contact", "account", "stage", "value")
    search_fields = ("deal", "account")
