# Generated by Django 4.2.4 on 2024-05-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
