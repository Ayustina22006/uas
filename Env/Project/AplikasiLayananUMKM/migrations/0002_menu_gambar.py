# Generated by Django 4.2.7 on 2023-11-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplikasiLayananUMKM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='gambar',
            field=models.ImageField(null=True, upload_to='static/assets/imgs/'),
        ),
    ]
