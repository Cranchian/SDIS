from django.urls import path

from .views import ProspectViewSet, UserCreate, LoginView


from rest_framework.routers import DefaultRouter

from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register("app", ProspectViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
]

urlpatterns += router.urls