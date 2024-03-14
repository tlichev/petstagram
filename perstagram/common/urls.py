from django.urls import path

from perstagram.common.views import index

urlpatterns = (
    path("", index, name="index"),

)