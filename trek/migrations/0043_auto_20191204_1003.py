# Generated by Django 2.2.5 on 2019-12-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trek', '0042_package_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusdetail',
            name='facebook_link',
            field=models.CharField(blank=True, help_text='Facebook link', max_length=500),
        ),
        migrations.AddField(
            model_name='aboutusdetail',
            name='instagram_link',
            field=models.CharField(blank=True, help_text='Instagram link', max_length=500),
        ),
        migrations.AddField(
            model_name='aboutusdetail',
            name='twitter_link',
            field=models.CharField(blank=True, help_text='Twitter link', max_length=500),
        ),
        migrations.AddField(
            model_name='aboutusdetail',
            name='youtube_link',
            field=models.CharField(blank=True, help_text='Youtube channel link', max_length=500),
        ),
    ]