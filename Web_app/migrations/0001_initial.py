# Generated by Django 5.1 on 2024-08-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('collage', models.CharField(max_length=30)),
                ('age', models.IntegerField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
