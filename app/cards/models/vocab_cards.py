# Python imports
from uuid import uuid4

# Django imports
from django.db import models


class VocabCards(models.Model):
    ''' model for storing data about texts
     and additional info about this texts 
     '''

    class Meta:
        ''' additional options for models '''
        app_label = "cards"
        verbose_name = "vocab_cards"
        db_table = "vocab_cards"
        ordering = ["-created_at"]
        unique_together = [["text", "text_definition"]]
        verbose_name = "vocab_cards"
        indexes = [models.Index(fields=["id"], name="vocab_id_index")]

    # main info fields for storing data 
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, db_column="id")
    text = models.CharField(max_length=256, null=True, editable=True, unique=False, db_column="word")
    text_definition = models.CharField(max_length=4096, null=True, editable=True, unique=False)
    # datetime fields to store date and time of create and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # additional info for future analytic
    points = models.DecimalField(decimal_places=10, max_digits=11, editable=True)
    iterations = models.PositiveIntegerField(default=0, null=True)
    status = models.CharField(null=True, max_length=32)

    def save(self, *args, **kwargs):
        ''' redefine logic of saving for counting iterations '''
        super().save(*args, **kwargs)
