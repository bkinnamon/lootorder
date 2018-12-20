# Generated by Django 2.1.4 on 2018-12-20 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lootlists', '0005_auto_20181220_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lootitem',
            name='taken',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taken_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
