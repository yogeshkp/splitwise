from django.urls import path
from . import views


urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("groups", views.group_creation, name="group"),
    # path("gotgroup", views.group_get, name="group_get"),
    path("shares", views.shares, name="shares"),
    path("debt", views.debts, name="debts")
]
