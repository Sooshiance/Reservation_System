from django.contrib import admin

from booking.models import Departure, Ticket, ReserveTicket


class DepartureAdmin(admin.ModelAdmin):
    list_display = ('date',)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ReserveTicketAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Departure, DepartureAdmin)

admin.site.register(Ticket, TicketAdmin)

admin.site.register(ReserveTicket, ReserveTicketAdmin)
