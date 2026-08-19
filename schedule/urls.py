from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"teams", views.TeamViewSet)
router.register(r"members", views.MemberViewSet)
router.register(r"shifts", views.ShiftViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
