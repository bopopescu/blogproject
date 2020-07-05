from django.urls import path
from blogapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('create/', views.create, name='create'),
    path('search/',views.search,name='search'),
    path('signup/',views.signup,name='signup'),
    path('update/<int:pk>/',views.Update.as_view(),name='update')
]
