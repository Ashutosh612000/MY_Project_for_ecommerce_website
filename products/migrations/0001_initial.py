# Generated by Django 4.2.2 on 2023-06-23 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('mobile', 'mobile'), ('charger', 'charger'), ('earphone', 'earphone')], default='mobile', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comapny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(choices=[('samsung', 'samsung'), ('vivo', 'vivo'), ('apple', 'apple'), ('google', 'google'), ('boat', 'boat')], default='apple', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product_description', models.TextField(max_length=500)),
                ('product_image', models.ImageField(upload_to='static/images/')),
                ('product_qunitity', models.PositiveIntegerField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('product_comapny', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.comapny')),
                ('product_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]