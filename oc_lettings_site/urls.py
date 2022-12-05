from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oc_lettings_app.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls'))
]


# Sentry test debug route
def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns += [
    path('sentry-debug/', trigger_error),
]
