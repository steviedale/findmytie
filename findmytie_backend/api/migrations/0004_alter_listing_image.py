# Generated by Django 5.1.3 on 2024-11-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_searchquery_host_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
