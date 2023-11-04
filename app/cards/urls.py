# Django imports
from django.urls import path

from cards.views import Cards

cards_actions = Cards.as_view({"post": "create"})

urlpatterns = [
    path("create/", cards_actions, name="create") 
]