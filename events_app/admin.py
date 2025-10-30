from django.contrib import admin
from .models import EventCategory, Event, Location, Title, Date

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]
    search_fields = ["title", "date"]
    list_filter = ["category"]
    date_hierarchy = "date"
    verbose_name = "Liveact"
    

    fieldsets = (
        ("Allgemein", {
            "fields": ("title", "category", "date"),
        }),
        ("Organisation", {
            "classes": ("collapse",),
            "fields": ("location", "capacity"),
        }),
    )
    

admin.site.register(Event, EventAdmin)

admin.site.register(EventCategory)

admin.site.register(Location)

admin.site.register(Title)

admin.site.register(Date)


