from django import forms

from .models import RoleModel, NewsArticle, FutureSelfRequest


class RoleModelsForm(forms.ModelForm):
    ethnicity_choices = (
        ("All", "All"),
        ("White", "White"),
        ("Mexican", "Mexican"),
        ("African", "African"),
        ("Mixed", "Mixed"),
    )

    gender_choices = (
        ("All", "All"),
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other"),
    )

    ethnicity = forms.ChoiceField(choices=ethnicity_choices, required=False)
    gender = forms.ChoiceField(choices=gender_choices, required=False)

    class Meta:
        model = RoleModel
        exclude = ('title', 'picture', 'position', 'description', 'url', 'name')


class NewsArticleForm(forms.ModelForm):

    class Meta:
        model = NewsArticle
        exclude = ("views", "date")


class FutureSelfForm(forms.ModelForm):

    class Meta:
        model = FutureSelfRequest
        fields = ('story', 'email')
