# Generated by Django 4.2.5 on 2023-10-08 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='name')),
                ('last_name', models.CharField(max_length=255, verbose_name='surname')),
                ('bio', models.TextField(blank=True)),
                ('birth_day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('time_create', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
        ),
    ]
