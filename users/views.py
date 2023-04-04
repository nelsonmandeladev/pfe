from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login

from documents.models import Documents
from requests.models import Requests
User = get_user_model()
# Create your views here.


def homePage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if password and email:
            try:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request, "Connection affectué avec succès")
                    return HttpResponseRedirect(reverse('account-home'))
                else:
                    messages.error(
                        request, "Mot de pass ou email incorrect")
                return HttpResponseRedirect(reverse('home'))
            except:
                messages.warning(
                    request, "Un problème est survenu lors de la connexion")
                return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(
                request, "Mot de pass et nom d'utilisateur requis pour se connecter")
            return HttpResponseRedirect(reverse('home'))
    return render(request, "users/login.html")


def accountHomePage(request):
    return render(request, "users/home-page.html")


def dashboardPage(request):
    users = User.objects.all().filter(is_superuser=False)[:5]
    documents = Documents.objects.all()
    requests = Requests.objects.all()
    bg_options = ["info", "main", "success", "danger", "warning"]
    context = {
        "documents": documents[:5],
        "requests": requests[:5],
        "documents_count": documents.count(),
        "requests_count": requests.count(),
        "requests_waiting_count": requests.filter(status="En Attente").count(),
        "requests_rejected_count": requests.filter(status="Rejettées").count(),
        "requests_validated_count": requests.filter(status="Validée").count(),
        "bg_options": bg_options,
        "users": users,
    }
    return render(request, "users/dashboard.html", context=context)


def listUsersPage(request):
    users = User.objects.all().filter(is_superuser=False)
    bg_options = ["info", "main", "success", "danger", "warning"]
    context = {
        "users": users,
        "bg_options": bg_options,
    }
    return render(request, "users/list-users.html", context=context)


def singleUserPage(request, user_id=None):
    user = None
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(
            request, f"Inpossible de trouver un utilisateur avec l'id {user_id}")
        return HttpResponseRedirect(reverse("list-users"))
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone = data.get("phone")
        role = data.get("role")
        address = data.get("address")
        region = data.get("region")
        town = data.get("town")
        zip_code = data.get("zip_code")
        is_active = data.get("is_active")

        if is_active == "on":
            is_active = True
        else:
            is_active = False

        try:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone
            user.role = role
            user.address = address
            user.region = region
            user.town = town
            user.zip_code = zip_code
            user.is_active = is_active
            user.save()
            messages.success(request, "Personnel modifié avec succès")
            return HttpResponseRedirect(reverse('list-users'))
        except:
            messages.error(
                request, "Un employé existe déjà avec le téléphone ou l'email que vous avez fourni")
            return redirect(f"/personnels/{user_id}")
    context = {
        "user": user
    }
    return render(request, "users/single-user.html", context=context)


def createUserPage(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone = data.get("phone")
        role = data.get("role")
        address = data.get("address")
        region = data.get("region")
        town = data.get("town")
        zip_code = data.get("zip_code")
        password = data.get("password")
        is_active = data.get("is_active")
        notify = data.get("notify")
        print(is_active)
        if is_active == "on":
            is_active = True
        else:
            is_active = False

        if not User.objects.filter(
            email=email
        ).exists():
            if not User.objects.filter(phone=phone).exists():
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    role=role,
                    address=address,
                    region=region,
                    town=town,
                    zip_code=zip_code,
                    is_active=is_active
                )
                user.set_password(password)
                user.save()
                messages.success(request, "Personnel ajouté avec succès")
                return HttpResponseRedirect(reverse('list-users'))
            else:
                messages.error(
                    request, "Un employé existe déjà avec le téléphone que vous avez fourni")
                return HttpResponseRedirect(reverse('create-user'))
        else:
            messages.error(
                request, "Un employé existe déjà avec l'email que vous avez fourni")
            return HttpResponseRedirect(reverse('create-user'))
    return render(request, "users/create-user.html")
