from django.contrib import admin
from .models import Participant, Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_filter = ["confirmed"]
    readonly_fields = ["booking_date"]


class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"full_name": ("first_name", "last_name")}


admin.site.register(Booking, BookingAdmin)

admin.site.register(Participant, ParticipantAdmin)



