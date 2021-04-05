from uuid import uuid4
from djongo import models

class TranslationMap(models.Model):
    class Meta:
        abstract = True

    source_place = models.PositiveIntegerField(null=True)
    coordinate = models.JSONField(max_length=2)
    translation = models.TextField()

class TranslationSubmission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sentences = models.TextField()
    maps = models.ArrayField(model_container=TranslationMap)
