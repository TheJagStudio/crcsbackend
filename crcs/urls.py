from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('djangoAdmin/', admin.site.urls),
    path("api/", include("main.urls")),
]
