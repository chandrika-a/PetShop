# Generated by Django 4.2.5 on 2023-10-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0002_alter_pet_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
