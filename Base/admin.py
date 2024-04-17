from django.contrib import admin
from .models import Student , Prof,Event,NewsLettre,Ticket
# Register your models here.
admin.site.register(Student)
admin.site.register(Prof)
admin.site.register(Event)
admin.site.register(NewsLettre)
admin.site.register(Ticket)