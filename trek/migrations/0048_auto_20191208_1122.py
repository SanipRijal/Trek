# Generated by Django 2.2.5 on 2019-12-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0047_activity_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecostexluded',
            name='excluded_items',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='packagecostincluded',
            name='included_items',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='packageitinerary',
            name='place_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
