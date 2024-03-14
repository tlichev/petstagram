from django.contrib import admin

from perstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_target_pets')

    @staticmethod
    def get_target_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])