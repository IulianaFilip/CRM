from django.contrib import admin

from .models import Account, Contact, Deal, Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("lead", "status", "email", "phone", "owner")
    search_fields = ("lead", "owner__username", "email")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("contact", "email", "phone", "priority")
    search_fields = ("contact", "email", "phone")


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("account", "email", "phone")
    search_fields = ("account", "email", "phone")


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("deal", "owner", "contact", "account", "stage", "value")
    search_fields = ("deal", "owner__username", "contact__contact", "account__account")
