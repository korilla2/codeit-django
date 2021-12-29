# Generated by Django 4.0 on 2021-12-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=50)),
                ('createdate', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('subject', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]