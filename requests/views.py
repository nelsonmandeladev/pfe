from django.shortcuts import render
from .models import Requests
from documents.models import Documents
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def listRequestPage(request):
    requests = Requests.objects.all()
    documents = Documents.objects.all()
    bg_options = ["info", "main", "success", "danger", "warning"]
    context = {
        "documents": documents,
        "requests": requests,
        "bg_options": bg_options,
    }
    return render(request, "requests/list-requests.html", context=context)


def createRequestPage(request, document_id):
    document = None
    try:
        document = Documents.objects.get(id=document_id)
    except Documents.DoesNotExist:
        messages.error(request, "Le model de document choisi n'existe pas !")
        return HttpResponseRedirect(reverse("list-requests"))

    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        content = data.get("content")

        save_request = Requests.objects.create(
            title=title,
            content=content
        )

        save_request.created_by = request.user
        save_request.from_document = document
        save_request.save()

        messages.success(
            request, f"Votre demandé : {title} a été enregistrée avec succès")
        return HttpResponseRedirect(reverse('list-requests'))

    context = {
        "template": document,
    }
    return render(request, "requests/create-requests.html", context=context)


def singleRequestPage(request, request_id):
    request_doc = None
    try:
        request_doc = Requests.objects.get(id=request_id)
    except Documents.DoesNotExist:
        messages.error(request, "Le model de document choisi n'existe pas !")
        return HttpResponseRedirect(reverse("list-requests"))

    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        content = data.get("content")

        request_doc.title = title,
        request_doc.content = content
        request_doc.save()

        messages.success(
            request, f"Votre demandé : {title} a été modifiée avec succès")
        return HttpResponseRedirect(reverse('list-requests'))

    context = {
        "request_doc": request_doc,
    }
    return render(request, "requests/single-request.html", context=context)
