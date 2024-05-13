import os

import matplotlib.pyplot as plt
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.templatetags.static import static

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


def generate_chart(months, counts):
    plt.figure(figsize=(10, 5))  # Define the size of the figure
    plt.plot(months, counts, marker="o", color="b", label="Registrations per Month")  # Plot the line chart
    plt.title("Monthly User Registrations")  # Add a title
    plt.xlabel("Month")
    plt.ylabel("Registrations")
    plt.legend()
    plt.grid(True)

    # Save the plot as a file
    fname = "user_registrations.png"
    chart_path = os.path.join(settings.MEDIA_ROOT, fname)
    plt.savefig(chart_path)
    plt.close()  # Close the plot to free up memory

    # Return the URL to the saved image
    return os.path.join(settings.MEDIA_URL, fname)


def dashboard_view(request):
    months = ["January", "February", "March", "April"]  # Example data
    counts = [10, 15, 20, 25]  # Example data

    chart_url = generate_chart(months, counts)
    template = loader.get_template("sales/home.html")
    context = {
        "chart_url": chart_url,
    }
    return HttpResponse(template.render(context, request))
