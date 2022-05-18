from django.contrib import admin
from musicians.models import Musician, Musicband, Album
from django.utils.html import format_html

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'instrument')
    list_display = ('first_name', 'last_name', 'instrument', 'colored_name', 'plays_guitar')
    search_fields = ['first_name', 'last_name', 'instrument']
    list_filter = ('instrument',)

    @admin.display(
        ordering='first_name',
        description='Full name in red',
    )
    def colored_name(self, obj):
        return format_html(
            '<span style="color: red;">{}</span>',
            obj.name,
        )

    @admin.display(boolean=True)
    def plays_guitar(self, obj):
        return 'Guitar' == obj.instrument

@admin.register(Musicband)
class MusicbandAdmin(admin.ModelAdmin):
    exclude = ('members',)
    list_filter = ('members',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['name', 'musicband__name']
