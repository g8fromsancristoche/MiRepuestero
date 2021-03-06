# Generated by Django 3.2.4 on 2021-12-21 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('firts_login', models.BooleanField(default=True)),
                ('VerifyID_1', models.BooleanField(default=False)),
                ('VerifyID_2', models.BooleanField(default=False)),
                ('use_dolar', models.BooleanField(default=False)),
                ('logo', models.ImageField(default='Repuestero_Media/logos/default-logo-repuestero.jpg', upload_to='Repuestero_Media/logos')),
                ('facade_photo', models.ImageField(default='Repuestero_Media/fachadas/default-fachada-repuestero.jpg', upload_to='Repuestero_Media/fachadas/')),
                ('name', models.CharField(max_length=50)),
                ('phone1', models.IntegerField(default=0)),
                ('phone2', models.IntegerField(default=0)),
                ('representative_name', models.CharField(max_length=50)),
                ('representative_id_number', models.IntegerField(default=0)),
                ('representative_phone', models.IntegerField(default=0)),
                ('representative_mail', models.EmailField(max_length=254)),
                ('rif_type', models.CharField(choices=[('1', 'V'), ('2', 'J'), ('3', 'E'), ('4', 'P'), ('5', 'G')], default='2', max_length=1)),
                ('rif', models.IntegerField(default=0)),
                ('rif_scan', models.ImageField(null=True, upload_to='Repuestero_Media/legales')),
                ('membership_type', models.CharField(choices=[('0', 'none'), ('1', 'Local'), ('2', 'expert'), ('3', 'unlimeted')], default='0', max_length=1)),
                ('voucher_scan', models.ImageField(null=True, upload_to='Repuestero_Media/pagos')),
                ('voucher_sended', models.BooleanField(default=False)),
                ('voucher_checked', models.BooleanField(default=False)),
                ('uses_bcv', models.BooleanField(default=False)),
                ('dolar_value', models.IntegerField(default=1)),
                ('favorite_seller', models.ManyToManyField(default=False, related_name='favorite_refiller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
