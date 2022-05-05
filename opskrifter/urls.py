from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('opskrift/<int:opskrift_id>/', opskrift),
    path('opskrifter/', opskrifter),
    path('ingredienser/', ingredienser),
]
