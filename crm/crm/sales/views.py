from django.shortcuts import render, get_object_or_404

from .models import Leads, Contacts, Accounts, Deals


def leads(request, lead_id):
    lead = get_object_or_404(Leads, pk=lead_id)
   
    context = {
        'lead': lead,
        
    }
        
     
    return render(request, 'sales/index.html', context)