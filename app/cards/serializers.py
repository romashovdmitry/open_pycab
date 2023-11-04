# DRf imports
from rest_framework import serializers

# models importss
from cards.models.vocab_cards import VocabCards


class CreateCardSerializer(serializers.ModelSerializer):
    ''' serializing data for creating cards '''

    class Meta:
        model = VocabCards
        fields = ["text", "text_definition"]