from django.db import models

# Choices for Priority
PRIORITY_CHOICES = (
    (1, "High"),
    (2, "Medium"),
    (3, "Low"),
)


class Ticket(models.Model):
    """Represents a ticket for project."""

    assigned_to = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="tickets",
        blank=True,
        null=True,
    )

    name = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    complete_by = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """str conversion"""
        return self.name
