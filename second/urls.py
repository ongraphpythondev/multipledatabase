from django.urls import path
from . import views
urlpatterns = [
    path('view', views.view),
    path('create', views.Create.as_view())
]
