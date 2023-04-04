from django.urls import path
from .views import (
    listDocumentPage,
    singleDocumentPage,
    createDocumentPage
)
urlpatterns = [
    path("", listDocumentPage, name="list-documents"),
    path("ajouter", createDocumentPage, name="create-document"),
    path("<str:document_id>", singleDocumentPage, name="single-document"),
]
