# Generated by Django 4.1.7 on 2023-04-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.CharField(choices=[('En Attente', 'En Attente'), ('Validée', 'Validée'), ('En Attente', 'En Attente')], default='waiting', max_length=255, null=True),
        ),
    ]
