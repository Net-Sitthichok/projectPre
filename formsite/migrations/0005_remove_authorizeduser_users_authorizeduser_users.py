# Generated by Django 4.2.4 on 2024-05-11 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formsite', '0004_alter_form_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorizeduser',
            name='users',
        ),
        migrations.AddField(
            model_name='authorizeduser',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
