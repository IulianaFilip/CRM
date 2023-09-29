from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Leads(models.Model):
    lead = models.CharField(max_length=100)
    status = models.CharField(
        max_length=100,
        choices=[("New", "New"), ("Contacted", "Contacted"), ("Converted", "Converted"), ("Lost", "Lost")],
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.lead

    class Meta:
        app_label = "crm.sales"


class Contacts(models.Model):
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    accounts = models.ManyToManyField("self", blank=True)
    priority = models.CharField(max_length=100, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])

    def __str__(self):
        return self.contact


class Accounts(models.Model):
    account = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.account


class Deals(models.Model):
    deal = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    stage = models.CharField(
        max_length=100, choices=[("Discovery", "Discovery"), ("Proposal", "Proposal"), ("Negotiation", "Negotiation")]
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.deal
