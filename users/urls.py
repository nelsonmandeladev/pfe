from django.urls import path
from .views import (
    homePage,
    accountHomePage,
    dashboardPage,
    listUsersPage,
    singleUserPage,
    createUserPage
)

urlpatterns = [
    path("", homePage, name="home"),
    path("accueil", accountHomePage, name="account-home"),
    path("tableau-de-bord", dashboardPage, name="dashboard"),
    path("personnels", listUsersPage, name="list-users"),
    path("personnels/ajouter", createUserPage, name="create-user"),
    path("personnels/<str:user_id>", singleUserPage, name="single-user"),
]
