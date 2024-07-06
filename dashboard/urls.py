from django.urls import path
from . import views

urlpatterns = [
    
    path('api/data/', views.get_data, name='get_data'),  # API to fetch data
    path('api/filter-options', views.get_filter_options, name='get_filter_options'),
]
