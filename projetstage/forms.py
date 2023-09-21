from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["titre", "category", "desc", "image"]
        labels = {
            "titre": "Titre",
            "category": "Catégorie",
            "desc": "Description",
            "image": "Image",
        }
        widgets = {
            "titre": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "desc": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
