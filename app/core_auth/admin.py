from django.contrib import admin

from core_auth.models import User, UserEvent, UserProfile

admin.site.register(User)
admin.site.register(UserEvent)
admin.site.register(UserProfile)
