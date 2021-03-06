# Generated by Django 3.2.4 on 2021-12-27 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('1', 'Bikes'), ('2', 'Cars'), ('3', 'Trucks')], default='1', max_length=1)),
                ('name', models.CharField(max_length=500)),
                ('part_number', models.CharField(max_length=280)),
                ('price', models.FloatField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('aka', models.CharField(max_length=280)),
                ('works_for', models.CharField(max_length=280)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.FileField(default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg', upload_to='Repuestero_Media/publicaciones/carros/')),
                ('image2', models.FileField(default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg', upload_to='Repuestero_Media/publicaciones/carros/')),
                ('image3', models.FileField(default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg', upload_to='Repuestero_Media/publicaciones/carros/')),
                ('image4', models.FileField(default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg', upload_to='Repuestero_Media/publicaciones/carros/')),
                ('image5', models.FileField(default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg', upload_to='Repuestero_Media/publicaciones/carros/')),
                ('favorite_of', models.ManyToManyField(default=False, related_name='favorite_part', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
