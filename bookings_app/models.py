from django.db import models

# Create your models here.
from events_app.models import Event


class Participant(models.Model):
    first_name = models.CharField(max_length=100, help_text="Please enter the participant's first name.")
    last_name = models.CharField(max_length=100, help_text="Please enter the participant's last name.")
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, help_text="Enter a valid email address for the participant.")

    def __str__(self):
        return self.full_name or f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"
