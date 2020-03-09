from django.urls import path

from .views import FrontAppView

urlpatterns = [
    path('', FrontAppView.as_view())
]
