from django.urls import path
from album import views

app_name = 'album'
urlpatterns = [
    path('get_all_album/', views.get_all_album, name='get_all_album'),
    path('edit_album/', views.edit_album, name='edit_album'),
    path('add_chapter/', views.add_chapter, name='add_chapter'),
    path('edit_chapter/', views.edit_chapter, name='edit_chapter'),
    path('get_chapter/', views.get_chapter, name='grt_chapter'),
]
