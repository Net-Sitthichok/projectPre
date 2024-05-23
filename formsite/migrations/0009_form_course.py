# Generated by Django 4.2.4 on 2024-05-14 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formsite', '0008_alter_clo_form_alter_templatedata_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='formsite.course'),
            preserve_default=False,
        ),
    ]