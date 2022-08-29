# Generated by Django 4.0.4 on 2022-06-28 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, choices=[('ST', 'Apply for staff post'), ('AD', 'Apply for admin post'), ('BW', 'Apply for blog writer post')], max_length=300, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('application_status', models.BooleanField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
