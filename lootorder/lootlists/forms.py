from dal import autocomplete
from django import forms
from .models import LootList, LootItem
from django.contrib.auth.models import User
from django.urls import reverse


class LootListForm(forms.ModelForm):
    guests = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='lootlists-user_search')
    )

    class Meta:
        model = LootList
        fields = ['name', 'description', 'guests']
