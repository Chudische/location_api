from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('get_name_by_id/', views.get_name_by_id, name='get_name_by_id'),
	path('get_full_name_by_id/', views.get_full_name_by_id, name='get_full_name_by_id'),
	path('get_most_popular_localities_by_names_first_leters/', views.get_most_popular_localities_by_names_first_leters, name='get_most_popular_localities_by_names_first_leters'),
]
