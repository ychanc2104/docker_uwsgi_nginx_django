# Generated by Django 3.1.4 on 2021-04-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]