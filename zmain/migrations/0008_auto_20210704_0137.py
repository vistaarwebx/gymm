# Generated by Django 3.2.4 on 2021-07-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zmain', '0007_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]