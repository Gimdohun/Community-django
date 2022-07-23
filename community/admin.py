from django.contrib import admin
from .models import Room, Issue, UserInfo
# Register your models here.
admin.site.register(Room)
admin.site.register(Issue)
admin.site.register(UserInfo)