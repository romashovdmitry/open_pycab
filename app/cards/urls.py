# Django imports
from django.urls import path

from cards.views import Cards

cards_actions = Cards.as_view({"post": "create", "patch":"partial_update"})

urlpatterns = [
    path("create/", cards_actions, name="create"),
    path("update/<uuid:card_id>/", cards_actions, name="update")
]