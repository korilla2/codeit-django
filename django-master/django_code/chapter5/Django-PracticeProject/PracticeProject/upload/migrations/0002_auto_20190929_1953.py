# Generated by Django 2.2.2 on 2019-09-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_path',
            field=models.FileField(upload_to='upload_files/%Y%m%d/'),
        ),
    ]