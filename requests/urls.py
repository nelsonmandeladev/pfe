from django.urls import path
from .views import (
    listRequestPage,
    createRequestPage,
    singleRequestPage
)

urlpatterns = [
    path("", listRequestPage, name="list-requests"),
    path("ajouter/<str:document_id>/", createRequestPage, name="create-request"),
    path("<str:request_id>", singleRequestPage, name="single-request"),
]
