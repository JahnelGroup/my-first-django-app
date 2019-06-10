from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/1/
    path('<int:todo_id>/', views.detail, name='detail')
]
