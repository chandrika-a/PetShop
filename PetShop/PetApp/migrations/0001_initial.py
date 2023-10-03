# Generated by Django 4.0.3 on 2023-10-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('weight', models.FloatField()),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]