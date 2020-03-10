from django import forms
from django_select2.forms import Select2Widget

from apps.user.models import User
from .models import Rework, Subject


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
        self.student = student  # type: User
        super(ReworkCreateForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(
            faculty=student.faculty,
            courses=student.group.course,
        )

    def save(self, commit=True):
        return Rework.objects.create(student=self.student, **self.cleaned_data)
