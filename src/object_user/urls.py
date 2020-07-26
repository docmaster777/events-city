from django.urls import path
from . import views

urlpatterns = [
    path('get-city-slug/', views.get_city_slug, name='get_city_slug'), # получение города при изменении
	# Select2
	path('get-county/', views.getCountry, name='get_country_select2'),  # получение Стран
	path('get-region/', views.getRegion, name='get_region_select2'),  # получение регионов
	path('get-city/', views.getCity, name='get_city_select2'),  # получение городов
]