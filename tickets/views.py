from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Ticket


class OpenTicketListView(TemplateView):
    """Show lists of open tickets by priority"""

    template_name = "ticket_list_open.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_context = {
            "open_high_tickets": Ticket.objects.filter(priority=1, completed=False),
            "open_medium_tickets": Ticket.objects.filter(priority=2, completed=False),
            "open_low_tickets": Ticket.objects.filter(priority=3, completed=False),
        }


class ClosedTicketListView(ListView):
    """Show list of closed tickets"""

    model = Ticket
    template_name = "ticket_list_closed.html"

    def get_queryset(self):
        return Ticket.objects.filter(completed=True)


class TicketCreateView(CreateView):
    """Create a new ticket"""

    model = Ticket
    template_name = "ticket_create.html"
    fields = "__all__"

    def get_success_url(self):
        """Where to send user on success"""
        messages.success(self.request, "Ticket Created Successfully")
        return reverse("open_ticket_list")


class TicketUpdateView(UpdateView):
    """Update a ticket"""

    model = Ticket
    template_name = "ticket_update.html"
    fields = "__all__"

    def get_success_url(self):
        """Where to send user on success"""
        messages.success(self.request, "Ticket Updated Successfully")
        return reverse("open_ticket_list")


class TicketDeleteView(DeleteView):
    """Delete a ticket"""

    model = Ticket
    template_name = "ticket_delete.html"

    def get_success_url(self):
        """Where to send user on success"""
        messages.success(self.request, "Ticket Deleted Successfully")
        return reverse("open_ticket_list")
