from django.forms import ModelForm
from .models import Note


class NoteCreationForm(ModelForm):

    class Meta:
        model = Note
        fields = ["title", "content", "role",]
