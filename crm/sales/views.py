from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Account, Contact, Deal, Lead


def home(request):
    leads = Lead.objects.all().order_by("-created_at")[:10]  # Get the latest 10 leads
    contacts = Contact.objects.all().order_by("-created_at")[:10]  # Same for contacts
    accounts = Account.objects.all().order_by("-created_at")[:10]  # And accounts
    deals_query = Deal.objects.select_related("owner", "contact", "account").order_by("-created_at")

    paginator = Paginator(deals_query, 10)
    page_number = request.GET.get("page")
    deals = paginator.get_page(page_number)

    context = {
        "leads": leads,
        "contacts": contacts,
        "accounts": accounts,
        "deals": deals,
    }

    return render(request, "sales/home.html", context)
