# Generated by Django 5.0.5 on 2024-05-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_productdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='CategoryImage',
            field=models.ImageField(blank=True, null=True, upload_to='Category Images'),
        ),
    ]