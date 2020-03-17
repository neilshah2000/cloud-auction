from django.urls import path
from . import views

urlpatterns = [
    path('getBidsForItem/<int:itemId>', views.getBidsForItem),
    path('bid/add/', views.BidCreate)
]
