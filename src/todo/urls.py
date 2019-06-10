from django.urls import path

from . import views

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/1/
    path('<int:todo_id>/', views.detail, name='detail')
]
