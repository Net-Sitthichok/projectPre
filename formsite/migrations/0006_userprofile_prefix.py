# Generated by Django 4.2.4 on 2024-05-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsite', '0005_remove_authorizeduser_users_authorizeduser_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='prefix',
            field=models.CharField(blank=True, max_length=10, verbose_name='คำนำหน้าชื่อ'),
        ),
    ]