# Generated by Django 4.1.7 on 2023-04-03 01:32

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
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(blank=True, max_length=10000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('last_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de mise à jour')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]