# Generated by Django 4.2.2 on 2023-06-17 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_assignements_options_assignements_details"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submission",
            name="Mark",
        ),
    ]
