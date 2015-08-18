from django.contrib import admin
from features.models import *
from interactions.models import *

# Register your models here.


class ObjectTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by']

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'object_type', 'today_prc']

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'object_type', 'today_prc']

class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'object_type']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment']

admin.site.register(ObjectType, ObjectTypeAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Comments, CommentsAdmin)