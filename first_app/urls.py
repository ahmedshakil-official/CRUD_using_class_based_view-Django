from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('musician_detail/<pk>/', views.MusicianDetails.as_view(), name='musician_detail'),
    path('add_musicians', views.AddMusician.as_view(), name='add_musician'),
    path('update_musicians/<pk>', views.UpdateMusician.as_view(), name='update_musician'),
    path('delete_musicians/<pk>', views.DeleteMusician.as_view(), name='delete_musician'),
]