from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('character/', views.character, name='character'),
    path('planets/', views.planets, name='planets'),
    path('planets/<int:pk>/', views.planet_detail_view, name='planet-detail'),
    path('update-data/', views.update_data, name='update-data'),
]