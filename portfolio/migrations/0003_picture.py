# Generated by Django 4.0.2 on 2022-03-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_testimonials_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Description', models.CharField(max_length=5000)),
                ('image_url', models.CharField(max_length=5000)),
            ],
        ),
    ]