# Generated by Django 4.2.6 on 2023-11-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0019_complaint_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
