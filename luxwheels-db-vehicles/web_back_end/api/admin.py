from django.contrib import admin
from .models import User, Reservation


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'name', 'email', 'contact_number', 'payment_method',
                    'insurance_plan', 'warranty', 'service_maintenance', 'comment', 'received_email')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Reservation, ReservationAdmin)
