from .models import Documents
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def listDocumentPage(request):
    documents = Documents.objects.all()
    bg_options = ["info", "main", "success", "danger", "warning"]
    context = {
        "documents": documents,
        "bg_options": bg_options,
    }
    return render(request, "documents/list-document.html", context=context)


def singleDocumentPage(request, document_id=None):
    if document_id is not None:
        document = None
        try:
            document = Documents.objects.get(id=document_id)
        except Documents.DoesNotExist:
            messages.info(
                request, f"Nous n'avons pas trouvé le document que vous cherchiez")
            return HttpResponseRedirect(reverse('list-document'))

        context = {
            "single_document": document
        }
    return render(request, "documents/single-document.html", context=context)


def createDocumentPage(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        document_type = data.get('document_type')
        content = data.get('content')
        user = request.user
        if not Documents.objects.filter(title=title).exists():
            document = Documents.objects.create(
                title=title,
                document_type=document_type,
                content=content
            )
            document.created_by = user
            document.save()
            messages.success(request, f"Document {title} creé avec succès")
            return HttpResponseRedirect(reverse('list-documents'))
        else:
            messages.error(
                request, f"Un autre document avec le même titre que {title} existe déjà")
            return redirect("/documents/ajouter")
    return render(request, "documents/create-document.html")
