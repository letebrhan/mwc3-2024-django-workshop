from django.urls import path

from .views import (
    OpenTicketListView,
)

urlpatterns = [
    path("", OpenTicketListView.as_view(), name="open_ticket_list"),
]
