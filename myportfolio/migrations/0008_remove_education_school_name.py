# Generated by Django 3.2.18 on 2023-04-14 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0007_education_school_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='school_name',
        ),
    ]