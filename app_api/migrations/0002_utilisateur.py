# Generated by Django 4.2.1 on 2023-06-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
    ]
