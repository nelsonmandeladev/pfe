from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Documents(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    TYPES = (
        ("letter", "Lettre"),
        ("ordonance", "Ordonance"),
        ("mission", "Ordre de mission"),
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )

    document_type = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        choices=TYPES,
        default='letter'
    )

    content = models.TextField(
        max_length=10000,
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        _('Date de création'), auto_now_add=True, null=True, blank=True)
    last_update = models.DateTimeField(
        _('Date de mise à jour'), auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
