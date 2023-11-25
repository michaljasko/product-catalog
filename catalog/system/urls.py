from django.urls import path
from system.views import import_data

urlpatterns = [
    path('import', import_data, name='import_data')
]