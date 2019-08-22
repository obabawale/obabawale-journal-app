from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path("", views.index, name="index" ),
    path("add/", views.add_journal, name="add_journal" ),
]