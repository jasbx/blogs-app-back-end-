# Generated by Django 5.0.1 on 2024-02-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degreeapp', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('discribtion', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
