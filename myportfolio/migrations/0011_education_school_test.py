# Generated by Django 3.2.18 on 2023-04-14 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0010_remove_education_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school_test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='school_test', to='myportfolio.school'),
            preserve_default=False,
        ),
    ]