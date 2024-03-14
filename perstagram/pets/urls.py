from django.urls import path, include

from perstagram.pets import views

urlpatterns = (
    path('add/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>', include([
        path("", views.pet_details, name='detail-pet'),
        path("edit/", views.pet_edit, name='edit-pet'),
        path("delete/", views.delete_pet, name='delete-pet'),
    ])),
)