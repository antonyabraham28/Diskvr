# Generated by Django 4.2.4 on 2023-08-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_neonlights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neonlights',
            name='ip_rating',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]