from django.shortcuts import render

# Create your views here.

def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def pet_photo_details(request, pet_id):
    return render(request, 'photos/photo-details-page.html')

def pet_photo_edit(request, pet_id):
    return render(request, 'photos/photo-edit-page.html')