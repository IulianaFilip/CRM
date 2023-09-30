from django.shortcuts import get_object_or_404, render

from .models import Accounts, Contacts, Deals, Leads


def home(request):
    leads = Leads.objects.all()
    contacts = Contacts.objects.all()
    accounts = Accounts.objects.all()
    deals = Deals.objects.all()

    context = {
        "leads": leads,
        "contacts": contacts,
        "accounts": accounts,
        "deals": deals,
    }

    return render(request, "home.html", context)
