from django.urls import path, include

from perstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>', include([
        path('', views.pet_photo_details, name='pet-details'),
        path('edit/', views.pet_photo_edit, name='pet-edit'),
    ])),
)