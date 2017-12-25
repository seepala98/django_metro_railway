from django.contrib import admin

from booking.models import Train, Station, Route, RoutePath, Ticket


class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'departure', 'arrival')
    search_fields = ('name', 'number')


class StationAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'destination')
    search_fields = ('name',)


class RoutePathAdmin(admin.ModelAdmin):
    list_display = ('route', 'station', 'order')
    list_filter = ('route', 'station')
    search_fields = ('route__name', 'station__name')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(RoutePath)
admin.site.register(Ticket, TicketAdmin)