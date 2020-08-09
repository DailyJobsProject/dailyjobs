# Generated by Django 3.0.3 on 2020-08-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200729_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contact_info',
            field=models.TextField(default='No social media available.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='about',
            field=models.TextField(default='No description available', max_length=1000),
        ),
    ]