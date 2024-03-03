from django.urls import path

from .views import (
    OpenTicketListView,
    ClosedTicketListView,
    TicketCreateView,
    TicketUpdateView,
    TicketDeleteView,
)

urlpatterns = [
    path("", OpenTicketListView.as_view(), name="open_ticket_list"),
    path("tickets/closed/", ClosedTicketListView.as_view(), name="closed_ticket_list"),
    path("tickets/create/", TicketCreateView.as_view(), name="ticket_create"),
    path("tickets/<int:pk>/update/", TicketUpdateView.as_view(), name="ticket_update"),
    path("tickets/<int:pk>/delete/", TicketDeleteView.as_view(), name="ticket_delete"),
]
