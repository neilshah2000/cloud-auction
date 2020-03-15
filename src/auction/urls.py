from django.urls import path
from . import views

urlpatterns = [
    path('getBidsForItem/<int:itemId>', views.getBidsForItem),
]
