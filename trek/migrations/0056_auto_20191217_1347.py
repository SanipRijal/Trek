# Generated by Django 2.2.5 on 2019-12-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0055_auto_20191216_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageitinerary',
            name='day',
            field=models.IntegerField(blank=True, help_text='Number of day(1, 2, 3, etc.)', null=True),
        ),
    ]
