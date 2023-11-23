# Generated by Django 4.2.7 on 2023-11-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
