from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import NoteCreationForm


# Create your views here.
class NoteListView(ListView):
    model = Note
    template_name = "notes/note-list.html"
    context_object_name = "notes"


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note-detail.html"
    context_object_name = "note"


def note_create_view(request):
    if request.method == "POST":
        form = NoteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note-list")

    else:
        form = NoteCreationForm()
        context = {
            "form": form,
        }

        return render(
            request,
            "notes/note-create.html",
            context
        )
