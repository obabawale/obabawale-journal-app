from django.urls import path
from . import views

app_name = 'journal'
urlpatterns = [
    path("", views.index, name="index" ),
    path("add/", views.add_journal, name="add_journal" ),
    path("delete/<int:journal_id>", views.delete_journal, name="delete_journal" ),
    path("edit/<int:journal_id>", views.edit_journal, name="edit_journal" ),
]
