# Generated by Django 3.2.4 on 2021-07-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zmain', '0004_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='detail',
            field=models.TextField(null=True),
        ),
    ]
