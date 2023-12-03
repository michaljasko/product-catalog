from django.urls import path
from system.views import import_data, model_detail

urlpatterns = [
    path('import', import_data, name='import_data'),
    path('detail/<str:model_name>/', model_detail, name='model_list'),
    path('detail/<str:model_name>/<int:item_id>', model_detail, name='model_detail'),
]