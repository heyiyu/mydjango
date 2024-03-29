# Generated by Django 2.1.5 on 2019-01-31 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_note_npicurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='nPicUrl',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='note',
            name='nTag',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='note',
            name='nTitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='摘要'),
        ),
    ]
