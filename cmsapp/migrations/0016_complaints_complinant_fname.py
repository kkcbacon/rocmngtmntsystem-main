# Generated by Django 4.2.14 on 2024-07-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0015_complaints_complaint_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='complinant_fname',
            field=models.CharField(default='Default Name', max_length=250),
        ),
    ]
