# Python imports
import logging

# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.validators import ValidationError

# import models
from cards.models.vocab_cards import VocabCards

# import serializers
from cards.serializers import CreateCardSerializer


class Cards(ModelViewSet):
    ''' class for processing text cards '''
    queryset = VocabCards.objects.all()
    serializer_class = CreateCardSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """ create new text card  """
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(
                data=serializer.validated_data,
                status=HTTP_201_CREATED
            )
        else:
            return ValidationError(
                detail=serializer.error_messages,
                code="validation_error"
            )

