# Generated by Django 3.0.3 on 2020-08-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_merge_20200730_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companypost',
            name='title',
            field=models.TextField(max_length=20),
        ),
    ]
