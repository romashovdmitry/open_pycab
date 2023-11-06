
# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.validators import ValidationError

# import models
from cards.models.vocab_cards import VocabCards

# import serializers
from cards.serializers import CreateCardSerializer

# import custom foos, classes
from cards.services import define_updated_fields


class Cards(ModelViewSet):
    ''' class for processing text cards '''
    queryset = VocabCards.objects.all()
    serializer_class = CreateCardSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'card_id'     

    def create(self, request, *args, **kwargs):
        """ create new text card  """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            return Response(
                data={
                    "card_id": instance.card_id,
                    "text": instance.text
                },
                status=HTTP_201_CREATED
            )

        else:
            raise ValidationError(
                detail=serializer.errors,
                code="validation_error"
            )

    def partial_update(self, request, *args, **kwargs):
        ''' update card, any mount of fields '''
        instance = self.get_object()
        previous_card = {
            "text": instance.text,
            "text_definition": instance.text_definition
        }
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            updated_fields = define_updated_fields(
                present_card={
                    "text": instance.text,
                    "text_definition": instance.text_definition
                },
                previous_card=previous_card
            )
            return Response(
                data={
                    "card_id": instance.card_id,
                    "updated_fields": updated_fields
                },
                status=HTTP_200_OK
            )

        else:
            raise ValidationError(
                detail=serializer.errors,
                code="validation_error"
            )
