from django.contrib import admin
from django.urls import include, path

from django.views.generic.base import RedirectView

urlpatterns = [
    path('basic_calc/', include('basic_calc.urls')),
    path('', RedirectView.as_view(url='/basic_calc/')),
    path('admin/', admin.site.urls),
]
