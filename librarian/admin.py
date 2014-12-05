from django.contrib import admin
from files.admin import AttachmentInlines

from .models import Book, Author


class SaveOwnerMixin(object):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()

    def get_readonly_fields(self, *args, **kwargs):
        defaults = super(SaveOwnerMixin, self).get_readonly_fields(*args,
                                                                   **kwargs)
        if 'owner' in defaults:
            return defaults
        fields = list(defaults)
        fields.append('owner')
        return fields


class BookAdmin(SaveOwnerMixin, admin.ModelAdmin):
    inlines = [AttachmentInlines]

    list_filter = ('publisher', 'year', 'language')
    date_hierarchy = "created"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


class AuthorAdmin(SaveOwnerMixin, admin.ModelAdmin):
    list_filter = ('name', 'surname')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
