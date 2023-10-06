# Generated by Django 4.2.5 on 2023-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(editable=False, max_length=36, primary_key=True, serialize=False)),
                ('product_name', models.CharField(editable=False, max_length=255)),
                ('product_image_path', models.CharField(editable=False, max_length=255)),
                ('username', models.CharField(editable=False, max_length=150)),
                ('email', models.EmailField(editable=False, max_length=254)),
                ('phone_number', models.CharField(editable=False, max_length=15)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]