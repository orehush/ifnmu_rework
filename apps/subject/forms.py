from django import forms
from django_select2.forms import Select2Widget

from .models import Rework


class ReworkCreateForm(forms.ModelForm):
    class Meta:
        model = Rework
        fields = (
            'subject',
            'document',
        )
        widgets = {
            'subject': Select2Widget()
        }

    def __init__(self, student, *args, **kwargs):
        self.student = student
        super(ReworkCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        return Rework.objects.create(student=self.student, **self.cleaned_data)
