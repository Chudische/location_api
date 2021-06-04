from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('get_name_by_id/', views.get_name_by_id, name='get_name_by_id'),
	path('get_full_name_by_id/', views.get_full_name_by_id, name='get_full_name_by_id'),
	path('get_ids_by_name/', views.get_ids_by_name, name='get_ids_by_name'),
	path('get_full_names_by_name/', views.get_full_names_by_name, name='get_full_names_by_name'),
	path('find_names/', views.find_names, name='find_names'),
	path('find_full_names/', views.find_full_names, name='find_full_names'),
	path('get_parents_id/', views.get_parents, name='get_parents_id'),
	path('get_affiliations_ids_by_id/', views.get_affiliations_ids_by_id, name='get_affiliations_ids_by_id'),
	path('get_name_with_affiliations_by_id/', views.get_name_with_affiliations_by_id, name='get_name_with_affiliations_by_id'),
	path('get_all_places_ids_in_location_area_by_id/', views.get_all_places_ids_in_location_area_by_id, name='get_all_places_ids_in_location_area_by_id'),
	path('all_locations_with_full_name/', views.all_locations_with_full_name, name='all_locations_with_full_name'),
	path('all_locations_without_area/', views.all_locations_without_area, name='all_locations_without_area'),
	path('all_locations_without_region/', views.all_locations_without_region, name='all_locations_without_region'),
	path('all_locations_have_child/', views.all_locations_have_child, name='all_locations_have_child'),
	
]

