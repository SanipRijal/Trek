# Generated by Django 2.2.2 on 2019-07-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0014_auto_20190702_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='country',
        ),
        migrations.AddField(
            model_name='review',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
