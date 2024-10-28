# Generated by Django 5.1 on 2024-10-14 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cidade.cidade')),
            ],
        ),
    ]