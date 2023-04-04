from django.db import models
from documents.models import Documents
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
import uuid
User = get_user_model()

# Create your models here.


class Requests(models.Model):
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
    title = models.CharField(
        max_length=255,
        null=True,
        blank=False
    )
    content = models.TextField(
        max_length=10000,
        null=True,
        blank=True
    )

    STATUS = (
        ("En Attente", "En Attente"),
        ("Validée", "Validée"),
        ("Rejettées", "Rejettées"),
    )

    status = models.CharField(
        max_length=255,
        choices=STATUS,
        blank=False,
        default="En Attente",
        null=True
    )

    from_document = models.ForeignKey(
        Documents,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        _('Date de création'), auto_now_add=True, null=True, blank=True)
    last_update = models.DateTimeField(
        _('Date de mise à jour'), auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return self.title
