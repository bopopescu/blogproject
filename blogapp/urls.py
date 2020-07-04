from django.urls import path
from blogapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('detail/<str:title>/',views.detail,name='detail'),
    path('create/', views.create.as_view(), name='create'),
    path('search/',views.search,name='search'),
    path('results/', views.results, name='results')
]
