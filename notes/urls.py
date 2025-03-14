from django.urls import path
from notes import views


urlpatterns = [
    path("", views.NoteListView.as_view(), name="note-list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
    path("create/", views.note_create_view, name="note-create"),
]
