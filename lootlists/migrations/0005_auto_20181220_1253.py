# Generated by Django 2.1.4 on 2018-12-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lootlists', '0004_auto_20181220_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lootlist',
            name='description',
            field=models.CharField(default='', max_length=256),
        ),
    ]
