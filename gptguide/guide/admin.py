from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(UserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["ref_code"].required = False
        return form

admin.site.register(UserCustomModel, UserAdmin)
admin.site.register(Rate)
admin.site.register(Pay)
admin.site.register(Message)
admin.site.register(AdminPanelEdit)
admin.site.register(WorkPiece)

