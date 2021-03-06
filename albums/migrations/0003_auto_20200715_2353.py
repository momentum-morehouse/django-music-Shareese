# Generated by Django 3.0.8 on 2020-07-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_init'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_title',
        ),
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default='unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(default='unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='released',
            field=models.DateField(default='2020-07-15'),
            preserve_default=False,
        ),
    ]
