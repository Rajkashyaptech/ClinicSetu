"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps.accounts.views import home_redirect
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home_redirect, name="home"),

    path("", include("apps.accounts.urls")),

    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("visits/", include("apps.visits.urls")),
    path("consultations/", include("apps.consultations.urls")),
    path("pharmacy/", include("apps.pharmacy.urls")),
    path("audit/", include("apps.audit.urls")),

    # APIs
    path("api/v1/accounts/", include("apps.accounts.api.urls")),
    path("api/v1/patients/", include("apps.patients.api.urls")),
    path("api/v1/visits/", include("apps.visits.api.urls")),
    path("api/v1/consultations/", include("apps.consultations.api.urls")),
    path("api/v1/prescriptions/", include("apps.prescriptions.api.urls")),
    path("api/v1/pharmacy/", include("apps.pharmacy.api.urls")),
    path("api/v1/medicines/", include("apps.medicines.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
