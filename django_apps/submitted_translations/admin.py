from django.contrib import admin

from .models import TranslationSubmission

# Register your models here.

class TranslationSubmissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(TranslationSubmission, TranslationSubmissionAdmin)
