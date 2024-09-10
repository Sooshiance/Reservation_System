from django.contrib import admin

from booking.models import Ticket, DisableDate, ReserveTicket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DisableDateAdmin(admin.ModelAdmin):
    list_display = ('date',)


class ReserveTicketAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Ticket, TicketAdmin)


admin.site.register(DisableDate, DisableDateAdmin)


admin.site.register(ReserveTicket, ReserveTicketAdmin)
