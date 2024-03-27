from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Lead(TimeStampedModel):
    lead = models.CharField(max_length=100)
    status = models.CharField(
        max_length=100,
        choices=[("New", "New"), ("Contacted", "Contacted"), ("Converted", "Converted"), ("Lost", "Lost")],
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads")

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __str__(self):
        return self.lead


class Contact(TimeStampedModel):
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    accounts = models.ManyToManyField("Account", blank=True, related_name="contacts")

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.contact


class Account(TimeStampedModel):
    account = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.account


class Deal(TimeStampedModel):
    deal = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, related_name="deals")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="related_deals")
    stage = models.CharField(
        max_length=100, choices=[("Discovery", "Discovery"), ("Proposal", "Proposal"), ("Negotiation", "Negotiation")]
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")

    def __str__(self):
        return self.deal
