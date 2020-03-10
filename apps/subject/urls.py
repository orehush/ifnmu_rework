from django.urls import path

from . import views


urlpatterns = [
    path('rework/create', views.ReworkCreateView.as_view(), name='rework-create'),
    path('rework/list', views.ReworkListView.as_view(), name='rework-list'),
    path('', views.IndexView.as_view(), name='index'),
]
