# Generated by Django 3.2.19 on 2023-05-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rasm', models.ImageField(upload_to='media')),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rasm', models.ImageField(upload_to='media')),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.category')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('rasm3', models.ImageField(blank=True, null=True, upload_to='media')),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.category')),
            ],
        ),
    ]
