from django.contrib import admin

from core_auth.models import Organizer, EventModel

admin.site.register(Organizer)
admin.site.register(EventModel)
