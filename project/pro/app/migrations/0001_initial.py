# Generated by Django 5.0 on 2023-12-21 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
