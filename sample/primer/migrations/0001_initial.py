# Generated by Django 3.1.4 on 2021-04-29 04:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='TPM', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadPrimer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='')),
                ('excel_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sequence', models.CharField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Primer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bottle_name', models.CharField(default='same with name', max_length=100)),
                ('sequence', models.CharField(max_length=500)),
                ('length', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)])),
                ('can_pcr', models.BooleanField(default=True)),
                ('L_pcr', models.IntegerField(default=0)),
                ('in_vector', models.BooleanField(default=True)),
                ('dir', models.CharField(default='none', max_length=10)),
                ('position', models.IntegerField(default=-1)),
                ('modification_5', models.CharField(default='none', max_length=200)),
                ('modification_3', models.CharField(default='none', max_length=200)),
                ('modification_internal', models.CharField(default='none', max_length=200)),
                ('who_ordered', models.CharField(max_length=50)),
                ('purpose', models.CharField(blank=True, max_length=200)),
                ('place', models.CharField(blank=True, default='Project box', max_length=50)),
                ('price', models.CharField(blank=True, max_length=50)),
                ('volumn', models.CharField(blank=True, max_length=50)),
                ('vendor', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edit_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='edit_by', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='primer.project')),
                ('vector', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vector', to='primer.vector')),
            ],
        ),
    ]
