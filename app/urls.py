from django.urls import path
from . import views

app_name ='app'
urlpatterns = [
    path('', views.index, name='index',),
    path('<int:memo_id>', views.detail, name='detail',),
    path('post', views.post, name='post'),
    path('about', views.about, name='about'),
    path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo')
]