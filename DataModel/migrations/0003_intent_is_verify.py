# Generated by Django 3.0.6 on 2020-06-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataModel', '0002_type_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='intent',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
