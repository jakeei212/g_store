# Generated by Django 3.1.3 on 2020-11-27 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',)},
        ),
    ]