from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class LootList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='guest_lists')
    name = models.CharField(max_length=256, default='')
    description = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lootlists-dashboard')


class LootItem(models.Model):
    list = models.ForeignKey(LootList, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    taken = models.ForeignKey(
        User,
        related_name='taken_items',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lootlists-list', kwargs={'pk': self.list_id})
