# Generated by Django 3.2.4 on 2021-07-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zmain', '0006_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
