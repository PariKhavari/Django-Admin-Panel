from django.db import models

# Create your models here.


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default="")

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Liveact"
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} ({self.date.date()})"


class Title(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Date(models.Model):
    date = models.DateField(help_text="Kalendertag des Termins")
    start_time = models.TimeField(
        null=True, blank=True, help_text="Beginn (optional)")
    end_time = models.TimeField(
        null=True, blank=True, help_text="Ende (optional)")

    def __str__(self):
        return f"{self.date()}"

