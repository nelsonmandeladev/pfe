# Generated by Django 4.1.7 on 2023-04-03 03:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_documents_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4742bcdb-7e41-467c-b104-f41f5244fceb'), editable=False, primary_key=True, serialize=False),
        ),
    ]