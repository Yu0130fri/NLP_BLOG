# Generated by Django 3.2.5 on 2021-08-08 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.user')),
                ('username', models.CharField(default='unknown', max_length=30)),
                ('zipcode', models.CharField(default='', max_length=8)),
                ('prefecture', models.CharField(default='', max_length=6)),
                ('city', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
