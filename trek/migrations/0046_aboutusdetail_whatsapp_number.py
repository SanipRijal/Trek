# Generated by Django 2.2.5 on 2019-12-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0045_auto_20191207_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusdetail',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
