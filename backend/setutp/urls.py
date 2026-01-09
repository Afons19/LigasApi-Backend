from django.urls import path, include

urlpatterns = [
    path('api/', include('liga_api.urls'))
]
