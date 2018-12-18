from django import forms
from .models import LootList, LootItem


class LootListForm(forms.ModelForm):
    class Meta:
        model = LootList
        fields = ['name', 'description']
