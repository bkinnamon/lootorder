from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class LootList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lootlists-dashboard')


class LootItem(models.Model):
    list = models.ForeignKey(LootList, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lootlists-list', kwargs={'pk': self.list_id})

    def should_show(self, user):
        if self.taken is False or self.list.user == user:
            return True
        else:
            return False
