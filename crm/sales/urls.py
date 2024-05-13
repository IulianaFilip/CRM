from django.urls import path

from .views import dashboard_view, home

app_name = "sales"

urlpatterns = [
    path("", home, name="home"),
    path("sales/", dashboard_view, name="dashboard"),
]

