# Generated by Django 3.2.4 on 2021-07-03 21:36

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zmain', '0002_rename_address_contactss_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30, null=True)),
                ('category', models.CharField(max_length=30, null=True)),
                ('date', models.DateField(null=True)),
                ('message', models.TextField(null=True)),
                ('content', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]
