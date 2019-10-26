from django import forms
from .models import RoleModel


class RoleModelsForm(forms.ModelForm):
    ethnicity_choices = (
        ("White", ("White")),
        ("Mexican", ("Mexican")),
        ("African", ("African")),
        ("Mixed", ("Mixed")),
    )

    gender_choices = (
        ("Female", ("Female")),
        ("Male", ("Male")),
        ("Other",("Other")),
    )

    ethnicity = forms.ChoiceField(choices=ethnicity_choices)
    gender = forms.ChoiceField(choices=gender_choices)

    class Meta:
        model = RoleModel
        exclude = ('title', 'picture', 'position','description','url')
