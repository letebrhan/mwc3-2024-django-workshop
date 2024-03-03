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
